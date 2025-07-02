import streamlit as st

st.title("🎈 Transformers Learning Challenge")
st.write("Khaled Fathy")


import tkinter as tk
from tkinter import simpledialog

# Create the root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user for input
st.user_input = simpledialog.askstring(title="Input", prompt="Please enter your input:")

# Print the user input
st.print("You entered:", user_input)


