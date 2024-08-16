import openai
import streamlit as st
from openai.error import AuthenticationError  # Import the correct exception

st.title("ChatGPT-like clone")

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the user input to OpenAI and get the response
    try:
        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messages
        )
        assistant_message = response['choices'][0]['message']['content']
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

        with st.chat_message("assistant"):
            st.markdown(assistant_message)

    except AuthenticationError:
        st.error("Authentication failed. Please check your API key.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
