import streamlit as st
import pickle
import streamlit_authenticator as stauth
import yaml


## REMOVE STREAMLIT HEADER AND FOOTER
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# --- USER AUTHENTICATION ---
from yaml.loader import SafeLoader
with open('auth/credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


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
    auth.logout(":material/logout:",'sidebar')
    st.sidebar.text("Developed by Aimana")


    # --- RUN NAVIGATION ---
    pg.run()

