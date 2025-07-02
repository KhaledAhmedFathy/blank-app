import streamlit as st
st.title("🎈 Transformers Learning Challenge")
st.write("Khaled Fathy")

# Prompt the user for input
st.user_input = simpledialog.askstring(title="Input", prompt="Please enter your input:")

# Print the user input
st.print("You entered:", user_input)


