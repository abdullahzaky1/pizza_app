import streamlit as st

st.title("Welcome to PizzaHub 🍕", anchor=False)
st.markdown("### The best pizza in town! Now serving fresh pasta and cool drinks.")

# Hero Image
st.image("https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=2070&auto=format&fit=crop", use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("🍽️ Hungry?")
        st.write("Browse our delicious selection of pizzas, pastas, and drinks.")
        if st.button("Explore Menu", use_container_width=True):
            st.switch_page("menu.py")

with col2:
    with st.container(border=True):
        st.subheader("✨ Need help?")
        st.write("Talk to our AI assistant to get nutrition facts and recommendations.")
        if st.button("Chat with AI", use_container_width=True):
            st.switch_page("chatbot.py")
