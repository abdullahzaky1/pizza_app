# 1. Importing extensions
import streamlit as st
import google.generativeai as ai
import speech_recognition as sr

# 2. Gemini API setup
api_key = 'AIzaSyDkjMi7ROthnGDQ4uYJmiDjNsrbs1XJIK0'
ai.configure(api_key='AIzaSyDkjMi7ROthnGDQ4uYJmiDjNsrbs1XJIK0')
model = ai.GenerativeModel(model_name='gemini-3.1-flash-lite-preview')

# 3. Page title
st.title('Chat with our AI✨', text_alignment='center')
st.subheader('Ask our AI anything about nutrition facts, food, etc.')

# 4. Transcribing audio
def transcribe_audio(file):
    # (1) Creating the listener
    listener = sr.Recognizer()
    
    # (2) Opening the audio file
    with sr.AudioFile(file) as audio:
        
        # (3) Recording the audio
        recording = listener.record(audio)
        
        # (4) Converting the recording into text
        text = listener.recognize_google(
            recording, language='en-US')
        return text 

# 5. Taking the user question
question = st.chat_input('Enter your question...', 
                         accept_audio=True)

if question: # If the question area is not empty
    
    # 1st chatting identity
    with st.chat_message('human'):
        if question.text:
            st.write(question.text)
        if question.audio:
            transcribed_text = transcribe_audio(question.audio)
            st.write(transcribed_text)
            question = question.text + transcribed_text
            
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
            'Pepperoni':280
                ]
            - Working hours: 8:00 AM to 12:AM
            '''
            answer = model.generate_content(prompt)
        st.write(answer.text)
        