import streamlit as st
st.title("🎈 Transformers Learning Challenge")
st.write("Khaled Fathy")
summarizer = pipeline("summarization", model="Falconsai/text_summarization")
print(summarizer(ARTICLE, max_length=1000, min_length=30, do_sample=False))
