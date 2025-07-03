import streamlit as st
st.title("🎈AI Summarization Web App")
st.write("Past your text & click summarize")
user_input = st.text_input("Text")
x = st.button("Summarize")
print(x)
AI_output = st.text_input("Summary")


from transformers import pipeline
summarizer = pipeline("summarization", model="t5-small")
st.title("🎈AI Summarization Web App")
st.write("Past your text & click summarize")
user_input = st.text_input("Text")
x = st.button("Summarize")
print(x)
prompt = "summarize:" + user_input
input = prompt
print(input)
output = summarizer(input,max_length=70)
print(output)
st.write(output)

