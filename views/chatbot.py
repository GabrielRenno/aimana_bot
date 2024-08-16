import openai
import streamlit as st

st.title("ChatGPT-like clone")

# Set your OpenAI API key
openai.api_key = "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"

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

    except openai.error.AuthenticationError:
        st.error("Authentication failed. Please check your API key.")
