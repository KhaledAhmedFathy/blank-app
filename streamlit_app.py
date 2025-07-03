import streamlit as st
st.title("🎈AI Summarization Web App")
st.write("Developed by Khaled Fathy")

y = st.button("Summary")
print(y)
user_input = st.text_input("What do you need to summarize")
x = st.button("Summarize")
print(x)


