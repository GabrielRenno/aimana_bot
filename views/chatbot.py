import streamlit as st
from views.chatbot_functions.response import response_generator
import time

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    # Refresh the page to clear the chat history
    st.rerun()


st.title("Talk with AImana Bot!")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    # Define the avatar based on the role
    avatar = ":material/smart_toy:" if message["role"] == "assistant" else ":material/person:"
    
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user", avatar=":material/person:"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar=":material/smart_toy:"):
        response = response_generator(prompt)  # Get the assistant's response
        # Stream the response word by word
        response_container = st.empty()
        for word in response.split():
            response_container.markdown(word + " ", unsafe_allow_html=True)
            time.sleep(2.05)
        response_container.markdown(response, unsafe_allow_html=True)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

