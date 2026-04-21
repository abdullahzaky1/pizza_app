# 1. Importing streamlit 
import streamlit as st

# 2. Converting the files into pages
home_page = st.Page(page='home.py', title='Home page', icon='🏠', default=True)
signin_page = st.Page(page='signin.py', title='Sign In', icon='🔑')
signup_page = st.Page(page='signup.py', title='Sign Up', icon='📝')
menu_page = st.Page(page='menu.py', title='Explore Menu', icon='🍽️')
chatbot_page = st.Page(page='chatbot.py', title='Talk with AI', icon='✨')
contact_page = st.Page(page='contact.py', title='Contact Us', icon='📞')

# 3. Creating the navbar
all_pages = st.navigation(
    pages=[home_page, signin_page, signup_page, menu_page, chatbot_page, contact_page],
    position='top'
)

# 4. Run all pages
all_pages.run()