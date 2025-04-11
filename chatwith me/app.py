#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyDmDtBz5Q96JzzJHojpyR2m0KJ44TKaZm8')

st.title('Chat with Me')
model = genai.GenerativeModel('gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

soru = st.text_input('You:')

if st.button('Ask'):
    response = chat.send_message(soru)
    st.write(response.text)
    st.write(chat.history)

if st.button('New Chat'):
    chat = model.start_chat(history=chat.history)