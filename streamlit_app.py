import streamlit as st

st.title("🎈AI Summarization Web App")
st.write("Past your text & click summarize")
user_input = st.text_input("Text")
x = st.button("Summarize")
print(x)
AI_output = st.text_input("Summary")
st.write(user_input).AI_output

prompt = "summarize:" + user_input
input = prompt
print(input)
##Summary = summarizer(input,max_length=70)
##print(output)

