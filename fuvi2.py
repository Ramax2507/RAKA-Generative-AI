import streamlit as st
import google.generativeai as genai

st.title("Welcome to the App")

genai.configure(api_key="AIzaSyBxbej54VRifGyHUARbSe8dSxJ1XK8jS0s")


text = st.text_input("Hey!! How do you want me to help you today?")

if text:
 
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    if st.button("Enter"):

         response = chat.send_message(text)
         st.write(response['text']) 
