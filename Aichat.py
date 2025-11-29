import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Gemini Chat Dashboard",
    page_icon="jg",
    layout="centered"
)
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter Google API Key", type="password")
    model_name = st.selectbox(
        "Select Model", 
        ["gemini-2.5-flash", "gemini-pro", "gemini-1.5-pro"]
    )
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("---")
    st.markdown("**Note:** Get your API key from [Google AI Studio](https://aistudio.google.com/).")
st.title("---ALPHA AI---")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to know?"):
    
    if not api_key:
        st.info("Please add your Google API Key in the sidebar to continue.")
        st.stop()
    st.session_state.messages.append({"role": "user", "content": prompt})
   
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"An error occurred: {e}")