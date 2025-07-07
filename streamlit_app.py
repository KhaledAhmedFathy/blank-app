import streamlit as st

st.title("🎈AI Summarization Web App")
st.write("Past your text & click summarize")
user_input = st.text_input("Text")
x = st.button("Summarize")
Click Me (x)
print(x)
#AI_output = st.text_input("Summary")
st.write(user_input,max_length=10)

prompt = "summarize:" + user_input
input = prompt
print(input)
##Summary = summarizer(input,max_length=70)
##print(output)


from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """https://blank-app-oqw4o31zmd.streamlit.app/"""

@app.route("/", methods=["GET", "POST"])
def index():
  #output = user_input
  #if request.method == "POST":
  #output = "Button was pressed!"
  #return render_template_string(HTML, output=output)
