import streamlit as st
st.title("🎈 Summarization App")
st.write("Khaled Fathy")
x = st.button("What do you need to summarize?")
print(x)
y = st.button("Summary")
print(y)
user_input = st.text_input("label goes here")


