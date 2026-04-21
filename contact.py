import streamlit as st

st.title("Contact Us 📞")
st.write("We would love to hear from you! Please reach out using the form below or visit us at our location.")

st.subheader("Our Location & Hours")
st.write("📍 **Address:** 123 Pizza Street, Food City, FC 12345")
st.write("⏰ **Working Hours:** 8:00 AM to 12:00 AM, Every Day")
st.write("✉️ **Email:** hello@pizzahub.com")

st.divider()

st.subheader("Send Us a Message")
with st.form("contact_form"):
    contact_name = st.text_input("Name")
    contact_email = st.text_input("Email")
    contact_message = st.text_area("Message")
    submit_msg = st.form_submit_button("Send Message", use_container_width=True)
    
    if submit_msg:
        if contact_name and contact_message:
            st.success(f"Thank you, {contact_name}! We have received your message and will get back to you soon.")
        else:
            st.error("Please fill in at least your name and message.")
