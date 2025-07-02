import streamlit as st
st.title("🎈 Transformers Learning Challenge")
st.write("Khaled Fathy")

from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

