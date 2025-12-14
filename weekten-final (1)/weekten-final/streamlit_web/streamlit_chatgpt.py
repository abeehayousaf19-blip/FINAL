# CST1510 Week 10 - ChatGPT API Integration with Streamlit
# File: streamlit_chatgpt.py

import streamlit as st
import openai
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Multi-Domain Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Multi-Domain Intelligence Platform")
st.subheader("CST1510 Week 10: ChatGPT API Integration")


with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API Key input
    api_key = st.text_input("OpenAI API Key:", type="password")
    
    # Model selection
    model = st.selectbox(
        "AI Model:",
        ["deepseek-ai/DeepSeek-V3.2", "meta-llama/Llama-3.2-3B-Instruct","gpt2-large"],
    )
    
    # Domain selection
    domain = st.selectbox(
        "Select Domain:",
        ["Cybersecurity", "Data Analysis", "IT Operations", "General"]
    )
    
    
    domain_prompts = {
        "Cybersecurity": "You are a cybersecurity expert specializing in threat detection, incident response, and security analysis.",
        "Data Analysis": "You are a data scientist expert in statistical analysis, data visualization, and insights generation.",
        "IT Operations": "You are an IT operations specialist focused on system monitoring, troubleshooting, and infrastructure management.",
        "General": "You are a helpful assistant for the Multi-Domain Intelligence Platform."
    }
    
    st.divider()
    st.caption(f"System Role: {domain_prompts[domain]}")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input(f"Ask about {domain}..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    
    if not api_key:
        with st.chat_message("assistant"):
            st.error("⚠️ Please enter your OpenAI API key in the sidebar.")
    else:
        
        with st.chat_message("assistant"):
            try:
                client = openai.OpenAI(api_key=api_key)
                
                # Prepare messages
                messages = [
                    {"role": "system", "content": domain_prompts[domain]}
                ] + [
                    {"role": msg["role"], "content": msg["content"]} 
                    for msg in st.session_state.messages
                ]
                
                # Stream the response with loading
                response_container = st.empty()
                full_response = ""
                
                with st.spinner("Getting response..."):
                    stream = client.chat.completions.create(
                        model=model,
                        messages=messages,
                        stream=True,
                        max_tokens=500
                    )
                    
                    for chunk in stream:
                        if chunk.choices[0].delta.content is not None:
                            full_response += chunk.choices[0].delta.content
                            response_container.markdown(full_response + "▌")
                
                response_container.markdown(full_response)
                
                
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please check your API key, credits, or internet connection.")

# Information section
with st.expander("ℹ️ About This Platform"):
    st.markdown("""
    **Multi-Domain Intelligence Platform - ChatGPT Integration**
    
    This platform integrates AI capabilities across three domains:
    1. **Cybersecurity**: Threat analysis, incident response guidance
    2. **Data Analysis**: Statistical insights, pattern recognition
    3. **IT Operations**: System troubleshooting, infrastructure advice
    
    **Instructions:**
    1. Get an OpenAI API key from platform.openai.com
    2. Enter the key in the sidebar
    3. Select your domain and start chatting
    4. Type 'clear' in chat to reset conversation
    """)


if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun()