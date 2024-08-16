import streamlit as st

def response_generator(prompt, messages):
    response = prompt
    messages = messages
    st.write(messages)
    return str(response)



