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

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Button Press Example</title>
</head>
<body>
    <h1>Press the Button</h1>
    <form method="POST">
        <button type="submit">Click Me!</button>
    </form>
    {% if output %}
        <p><strong>Output:</strong> {{ output }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
  #output = user_input
    if request.method == "POST":
        output = "Button was pressed!"
    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    app.run(debug=True)
