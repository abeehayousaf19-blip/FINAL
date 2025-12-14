# ChatGPT API Integration Project

A collection of Python scripts demonstrating OpenAI ChatGPT API integration using console applications and Streamlit web interfaces.

## Project Structure

```
├── basic_console/          # Console-based applications
│   ├── chatgpt_basic.py
│   ├── chatgpt_interactive.py
│   └── chatgpt_secure.py
├── streamlit_web/          # Streamlit web applications
│   ├── chatgpt_streamlit_streaming.py
│   └── streamlit_chatgpt.py
├── chatgpt_streamlit.py     # Basic Streamlit app (root)
├── requirements.txt
└── README.md
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API key:**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Get your API key from: https://platform.openai.com/api-keys

## How to Run

### Console Applications (basic_console/)

**Basic Script:**
```bash
python basic_console/chatgpt_basic.py
```
Simple one-time question/answer script.

**Interactive Chat:**
```bash
python basic_console/chatgpt_interactive.py
```
Interactive console chat. Type `quit` to exit.

**Secure Client:**
```bash
python basic_console/chatgpt_secure.py
```
Module for secure API key handling (used by other scripts).

### Streamlit Web Applications

**Basic Streamlit App (Root):**
```bash
streamlit run chatgpt_streamlit.py
```
Simple chat interface with model selection and temperature control.

**Streaming Chat (streamlit_web/):**
```bash
streamlit run streamlit_web/chatgpt_streamlit_streaming.py
```
Chat interface with real-time streaming responses.

**Multi-Domain Platform (streamlit_web/):**
```bash
streamlit run streamlit_web/streamlit_chatgpt.py
```
Advanced platform with domain-specific AI assistants (Cybersecurity, Data Analysis, IT Operations).

## Features

- **Console Apps**: Simple command-line interfaces for ChatGPT
- **Streamlit Apps**: Interactive web interfaces with chat history
- **Streaming**: Real-time response streaming for better UX
- **Multi-Domain**: Specialized AI assistants for different domains
- **Secure**: Environment variable-based API key management

## Notes

- All applications require a valid OpenAI API key
- Console apps use `.env` file for API key
- Streamlit apps can use `.env` or Streamlit secrets
- Each module is independent (separation of concerns)

