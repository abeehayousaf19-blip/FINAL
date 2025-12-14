import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
try:
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=st.secrets['OPENAI_API_KEY']
        )
except:
    client = None

# Page setup
st.set_page_config(page_title='ChatGPT Assistant', page_icon='💬')
st.title('💬 ChatGPT - OpenAI API')

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'}
    ]

# Sidebar controls
with st.sidebar:
    if st.button('Clear chat'):
        st.session_state.messages = [
            {'role': 'system', 'content': 'You are a helpful assistant.'}
        ]
        st.rerun()

    model = st.selectbox(
        "Model",
        ["deepseek-ai/DeepSeek-V3.2", "meta-llama/Llama-3.2-3B-Instruct","gpt2-large"],
        index=0
    )

    temperature = st.slider("Temperature", 0.0, 2.0, 1.0, 0.1)

# Display chat history
for msg in st.session_state.messages:
    if msg['role'] != 'system':
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])

# User input
prompt = st.chat_input("Say something...")
if prompt:
    # Show user message
    with st.chat_message('user'):
        st.markdown(prompt)

    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # Show assistant message with loading
    with st.chat_message('assistant'):
        if not client:
            st.error("⚠️ Please set OPENAI_API_KEY in Streamlit secrets")
        else:
            with st.spinner("Thinking..."):
                try:
                    # Get assistant response
                    completion = client.chat.completions.create(
                        model=model,
                        messages=st.session_state.messages,
                        temperature=temperature
                    )
                    response = completion.choices[0].message.content
                    st.markdown(response)
                    st.session_state.messages.append({'role': 'assistant', 'content': response})
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.info("Please check your API key or internet connection.")
