import streamlit as st
import pandas as pd
import tkinter as tk


# collecting data to store in Employee.db
st.title ('ML Deployment App')
Input_text1 = st.text_input('Name') 
Input_text2 = st.text_input('Age') 
Input_text3 = st.text_input('Average Income') 

Output_Language = st.selectbox('Select between LOW, MEDIUM, HIGH',options= 'LMH')


root = tk.Tk()
root.title("Button Example")
def button_clicked():
    print("Submit!")
# Create a button and attach the function to it
button = tk.Button(root, text="Submit!", command=button_clicked)
button.pack(pady=20)

# Run the application
root.mainloop()