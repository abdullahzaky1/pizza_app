import streamlit as st

# Initialize session states
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'name' not in st.session_state:
    st.session_state['name'] = None
if 'phone' not in st.session_state:
    st.session_state['phone'] = None

# If user is already logged in
if st.session_state['logged_in']:
    st.success(f"You are already logged in as {st.session_state['name']}!")
    if st.button("Go to Menu", use_container_width=True):
        st.switch_page("menu.py")
    if st.button("Log out"):
        st.session_state['logged_in'] = False
        st.session_state['name'] = None
        st.session_state['phone'] = None
        st.rerun()
else:
    st.title("Sign In 🔑")
    st.write("Please sign in to access the menu.")
    
    with st.form("signin_form"):
        email = st.text_input("Email", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password")
        
        submit = st.form_submit_button("Sign In", use_container_width=True)
        
        if submit:
            if email and password:
                st.session_state['logged_in'] = True
                # If they didn't sign up but bypassed, we provide generic Customer name
                if not st.session_state.get('name'):
                    st.session_state['name'] = "Customer"
                st.switch_page("menu.py")
            else:
                st.error("Please enter your email and password.")
                
    st.divider()
    st.write("Don't have an account?")
    if st.button("Sign Up Here", use_container_width=True):
        st.switch_page("signup.py")
