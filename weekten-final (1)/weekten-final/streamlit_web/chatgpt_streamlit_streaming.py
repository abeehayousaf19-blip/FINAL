import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    api_key = st.secrets.get('OPENAI_API_KEY', '')

client = OpenAI(api_key=api_key) if api_key else None

model = "deepseek-ai/DeepSeek-V3.2"  
temperature = 0.7


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]


for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


prompt = st.chat_input("Ask something...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("assistant"):
        if not client:
            st.error("⚠️ Please set OPENAI_API_KEY in .env file or Streamlit secrets")
        else:
            try:
                container = st.empty()
                full_reply = ""
                
                
                with st.spinner("Getting response..."):
                    stream = client.chat.completions.create(
                        model=model,
                        messages=st.session_state.messages,
                        temperature=temperature,
                        stream=True
                    )

                    for chunk in stream:
                        delta = chunk.choices[0].delta
                        if delta.content:
                            full_reply += delta.content
                            container.markdown(full_reply + "▌")

                container.markdown(full_reply)

                
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_reply}
                )
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please check your API key or internet connection.")
