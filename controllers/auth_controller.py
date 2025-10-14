import streamlit as st
from models.user_model import create_user, get_user_by_username

# Decorator to validate input
def validate_input(func):
    def wrapper(username, password, *args, **kwargs):
        if not username or not password:
            st.error("Username and password are required.")
            return False
        if len(password) < 6:
            st.error("Password must be at least 6 characters.")
            return False
        return func(username, password, *args, **kwargs)
    return wrapper

@validate_input
def handle_login(username, password):
    user = get_user_by_username(username)
    if user and user["password"] == password:
        st.session_state["logged_in"] = True
        st.session_state["user_id"] = user["user_id"]
        st.session_state["username"] = user["username"]
        return True
    st.error("Invalid credentials.")
    return False

@validate_input
def handle_signup(username, password, email):
    if get_user_by_username(username):
        st.error("Username already exists.")
        return False
    create_user(username, password, email)
    return handle_login(username, password)



