import streamlit as st
import google.generativeai as genai


st.title("welcome to RAKA Gen AI")

genai.configure(api_key="AIzaSyBxbej54VRifGyHUARbSe8dSxJ1XK8jS0s")  

text = st.text_input("Hey!! How do you want me to help you today?")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
