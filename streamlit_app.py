import streamlit as st
st.title("🎈 Transformers Learning Challenge")
st.write("Khaled Fathy")


import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

# Function to get a response from the OpenAI API
def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Prompt the user for input
user_input = input("Please enter your input: ")

# Get the response from the OpenAI API
response = get_response(user_input)

# Print the response
print("Copilot response:", response)

