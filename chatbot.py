# 1. Importing extensions
import streamlit as st
import google.generativeai as ai

# 2. Gemini API setup
model_name = 'gemini-3.1-flash-lite-preview'
api_key = 'AIzaSyDkjMi7ROthnGDQ4uYJmiDjNsrbs1XJIK0'

ai.configure(api_key='AIzaSyDkjMi7ROthnGDQ4uYJmiDjNsrbs1XJIK0')
model = ai.GenerativeModel(model_name='gemini-3.1-flash-lite-preview')

# 3. Page title
st.title('Chat with our AI✨', text_alignment='center')
st.subheader('Ask our AI anything about nutrition facts, food, etc.')

# 4. Taking the user question
question = st.chat_input('Enter your question...', 
                         accept_audio=True, accept_file=True)

if question: # If the question area is not empty
    # 1st chatting identity
    with st.chat_message('human'):
        st.write(question)
    
    # 2nd chatting identity 
    with st.chat_message('ai'):
        with st.spinner(text='Generating...✨'):
            prompt = f'''
            Answer this question:
            {question}
            But consider the following:
            - Do not answer any question irrelevant to food and 
            nutrition.
            - This is the menu of our restaurant:
                menu = [
            'Chicken':250,
            'Margerita':210, 
            'Pepperoni':280,
            'Burger':320
                ]
            - Working hours: 8:00 AM to 12:AM
            '''
            answer = model.generate_content(prompt)
        st.write(answer.text)
        