import streamlit as st
st.title("🎈AI Summarization Web App")
st.write("Past your text & click summarize")
user_input = st.text_input("Text")
x = st.button("Summarize")
print(x)
AI_output = st.text_input("Summary")


