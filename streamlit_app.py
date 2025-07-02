import streamlit as st
st.title("🎈 Transformers Learning Challenge")
st.write("Khaled Fathy")
st.summarizer = pipeline("summarization", model="t5-small")

