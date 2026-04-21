import streamlit as st

st.title("Create Account 📝")
st.write("Join PizzaHub today!")

with st.form("signup_form"):
    st.write("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email", placeholder="example@gmail.com")
    with col2:
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
    
    st.write("Delivery Details")
    col3, col4 = st.columns([3, 1])
    with col3:
        address = st.text_input("Street Address")
    with col4:
        apt = st.text_input("Apartment No.")
        
    submit = st.form_submit_button("Sign Up", use_container_width=True)
    
    if submit:
        if name and email and password and address:
            st.session_state['name'] = name
            st.session_state['phone'] = phone
            st.session_state['email'] = email
            st.session_state['address'] = f"{address}, Apt {apt}"
            st.success(f"Account created successfully for {name}! Please sign in.")
            # st.switch_page is wrapped in a container or rerun may be needed but this usually works
            st.switch_page("signin.py")
        else:
            st.error("Please fill in all required fields (Name, Email, Password, Address).")

st.divider()
st.write("Already have an account?")
if st.button("Sign In Here", use_container_width=True):
    st.switch_page("signin.py")
