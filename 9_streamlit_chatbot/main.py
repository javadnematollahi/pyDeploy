import streamlit as st
from database import Sqlmethods
import time
import json
import asyncio
import requests


async def ai(text, history):
    global ai_result
    # headers = {"Authorization": f"Bearer {os.getenv('token')}"}
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYmRjYmY4NzEtZjdhNC00MDQ3LThjYWItZDc2OWI0YTExNWNhIiwidHlwZSI6ImZyb250X2FwaV90b2tlbiJ9.vnx4cBCXSNxTaavf3H0D9mEkFu5mOQm8w7RaaBTYuuk"}

    print(history)
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": f"{text}",
        "chatbot_global_action": "Act as an assistant",
        "previous_history": history,
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    ai_result = json.loads(response.text)['openai']['generated_text']

if "dbmethods" not in st.session_state:
    st.session_state.dbmethods = Sqlmethods()
    st.session_state.dbmethods.create_db_and_tables()

def main():
    if "page" not in st.session_state: 
        st.session_state.page = "Sign In"

    if st.session_state.page == "Chatroom":
        asyncio.run(chat_page())
    elif st.session_state.page == "Sign In":
        sign_in_page()
    elif st.session_state.page == "Sign Up":
        sign_up_page()

def sign_in_page():
    with st.sidebar:
        st.write("This is a chatbot with AI\nYou can sign in and use it in free.")

    st.title("Sign In Page")

    st.subheader("Enter your username and password:")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        if username and password:
            result = st.session_state.dbmethods.select_a_user(username, password)
            if not result:
                st.error("Please Sign up first.")
            else:
                st.success("You have successfully signed in!")
                if "user" not in st.session_state:
                    st.session_state.user = result
                    print(st.session_state.user)
                st.session_state.page = "Chatroom"
                st.rerun()
        else:
            st.error("Please fill out all fields.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("still not registred:")
    with col2:
        if st.button("Sign Up"):
            print("signup")
            st.session_state.page = "Sign Up"
            st.rerun()

def sign_up_page():
    with st.sidebar:
        st.write("This is a chatbot with AI\nYou can sign up and use it in free.")

    st.title("Sign Up Page")

    st.subheader("Create your account")

    # Input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    not_a_robot = st.checkbox("I am not a robot")

    # Sign Up button
    if st.button("Sign Up"):
        if username and password and email and not_a_robot:
            st.session_state.dbmethods.add_user(username=username, password=password, email=email)
            st.success("You have successfully signed up!\nYou automatically return to log in page...")
            time.sleep(2)
            st.session_state.page = "Sign In"
            st.rerun()
        elif not not_a_robot:
            st.error("Please confirm you are not a robot.")
        else:
            st.error("Please fill out all fields.")

    if st.button("Back"):
        st.session_state.page = "Sign In"
        st.rerun()

def history(user):
    message_user, message_ai = st.session_state.dbmethods.select_message_of_a_user(user=user)
    chat_history = []
    if message_user != "" and message_ai != "":
        user_list = message_user.split(',')
        ai_list = message_ai.split(',')
        if len(user_list)>3 and len(ai_list)>3:
            user_list = user_list[-3:]
            ai_list = ai_list[-3:]
        for u_message, a_message in zip(user_list, ai_list):
            user_dict = {}
            ai_dict = {}
            user_dict['role'] = 'user'
            user_dict['message'] = u_message
            ai_dict['role'] = 'assistant'
            ai_dict['message'] = a_message
            chat_history.append(user_dict)
            chat_history.append(ai_dict)
    return chat_history



async def chat_page():
    with st.sidebar:
        st.title("Welcome to chatbot")
        st.subheader(f"Hello {st.session_state.user.usernames}")
        if st.button("Sign Out"):
            st.session_state.page = "Sign In"
            st.rerun()
    messages = st.container()
    if prompt := st.chat_input("Say something"):
        chat_history = history(st.session_state.user)
        await asyncio.create_task(ai(prompt, chat_history))
        print("texxxxxxxxxxt: ",ai_result)
        st.session_state.dbmethods.update_message_of_a_user(message_user=prompt, message_ai=ai_result, user=st.session_state.user)
        message_user, message_ai = st.session_state.dbmethods.select_message_of_a_user(user=st.session_state.user)
        for u_message, a_message in zip(message_user.split(','), message_ai.split(',')):
            messages.chat_message("user").write(u_message)
            messages.chat_message("assistant").write(f"{a_message}")

if __name__ == "__main__":
    main()