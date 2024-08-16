import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import yaml


# --- USER AUTHENTICATION ---
from yaml.loader import SafeLoader
with open('auth/credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
#Load hashed passwords
file_path = "auth/hashed.pkl"
with open(file_path, "rb") as file:
    hashed_passwords = pickle.load(file)

#Create authenticator
auth = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)


name, authentication_status, username = auth.login('main')


if authentication_status == False:
    st.error("Username or password is incorrect. Please try again.")

if authentication_status == None:
    st.warning("Please enter your username and password.")

if authentication_status == True:

    # --- PAGE SETUP ---
    login_page = st.Page(
        page = "views/about.py",
        title = "Aimana",
        icon = ":material/account_circle:", #https://fonts.google.com/icons
        default = True
    )

    chatbot_page = st.Page(
        page = "views/chatbot.py",
        #title = "Chatbot",
        icon = ":material/smart_toy:" 
    )


    # --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
    pg = st.navigation(pages = [login_page, chatbot_page])

    # --- NAVIGATION SETUP [WITH SECTIONS] ---
    pg = st.navigation(
        {
            "About": [login_page],
            "Funtionalities": [chatbot_page]
        })

    # --- SHARED ON ALL PAGES ---
    st.logo("assets/logo.jpeg")
    st.sidebar.text("Developed by Aimana")


    # --- RUN NAVIGATION ---
    pg.run()

