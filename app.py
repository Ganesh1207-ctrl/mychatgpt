import streamlit as st
from datetime import datetime
import requests
import json
from callollama import callOLLAMA

st.set_page_config(
    page_title="chatbot",
)

if "messages" not in st.session_state:
    st.session_state_messages=[]
    st.session_state_messages.append(
        {
        "role":"assistant",
        "content":"Hello I am smart chatbot.How can I help you today?"
        }
    )

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

st.title("Offline LLM")
st.markdown("Welcome to session 2 of offline GPT ")

st.subheader("chat here")

for message in st.session_state_messages    :
    if message["role"]=="user":
        st.info(message["content"])
    else:
        st.success(message["content"])

if st.session_state.is_typing:
    st.markdown("Bot is typing...")
    st.warning("Typping...")

st.markdown("----")
st.subheader("Your Message")

with st.form(key="chat_form",clear_on_submit=True):
    user_input=st.text_input(
        "Type ypur message",
        placeholder="Ask me anything..."
    )
    send_button=st.form_submit_button("Send message",type="primary")

col1, col2=st.columns([1,1])
with col1:
    clear_button=st.button("clear chat")
if send_button and user_input:
    st.session_state_messages.append(
        {
            "role":"user",
            "content":user_input.strip()
        }
    )
    st.session_state_is_typing=True
    st.rerun()

if st.session_state.is_typing:
    user_message=st.session_state_messages[-1]["content"]
    bot_response=callOLLAMA(user_message)
    st.session_state_messages.append(
        {
            "role":"assistant",
            "content": bot_response
        }
    )
    st.session_state.is_typing= False
    st.rerun()
