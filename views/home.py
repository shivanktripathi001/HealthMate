# import streamlit as st

# from views.login import render as login_render
# from views.signup import render as signup_render
# from views.symptom_checker import render as symptom_render
# from views.remedies import render as remedy_render
# from views.appointment import render as appointment_render
# from views.dashboard import render as dashboard_render


# def home():

#     def load_css():
#         with open("style.css") as f:
#             st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#     load_css()

#     st.sidebar.title("HealthMate Navigation")
#     page = st.sidebar.radio("Go to", [
#         "Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment", "Dashboard"
#     ])

#     if st.session_state.get("logged_in"):
#         if st.sidebar.button("Logout"):
#             st.session_state.clear()
#             st.experimental_rerun()

#     if page == "Login":
#         login_render()
#     elif page == "Sign Up":
#         signup_render()
#     elif page == "Symptom Checker":
#         symptom_render()
#     elif page == "Remedies":
#         remedy_render()
#     elif page == "Appointment":
#         appointment_render()
#     elif page == "Dashboard":
#         dashboard_render()


# import streamlit as st
# from views.login import render as login_render
# from views.signup import render as signup_render
# from views.symptom_checker import render as symptom_render
# from views.remedies import render as remedy_render
# from views.appointment import render as appointment_render
# from views.dashboard import render as dashboard_render
 
# def load_css():
#     """Loads and injects a local CSS file and Google Fonts."""
#     try:
#         with open("style.css") as f:
#             st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#         st.markdown(
#             """
#             <link rel="preconnect" href="https://fonts.googleapis.com">
#             <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
#             <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
#             """,
#             unsafe_allow_html=True
#         )
#     except FileNotFoundError:
#         st.error("`style.css` not found. Please create the file in the same directory.")
 
# def home():
#     """Main function to run the Streamlit application."""
#     load_css()
 
#     # --- SIDEBAR HEADER AND DYNAMIC CONTENT ---
#     st.sidebar.markdown(
#         """
#         <div class="custom-logo">
#             <h1>HealthMate</h1>
#             <p>"HEALTH IS WEALTH"</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
 
#     # Dynamic Welcome/Profile Section
#     if st.session_state.get("logged_in") and "username" in st.session_state:
#         st.sidebar.markdown(f"<div class='profile-info'>Hello, {st.session_state.username}!</div>", unsafe_allow_html=True)
    
#     st.sidebar.markdown("---")
 
#     # --- NAVIGATION ---
#     if "page" not in st.session_state:
#         st.session_state.page = "Login"
 
#     page = st.sidebar.radio(
#         "Go to",
#         ["Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment", "Dashboard"],
#         index=["Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment", "Dashboard"].index(st.session_state.page),
#     )
 
#     if page != st.session_state.page:
#         st.session_state.page = page
#         st.rerun()
 
#     if st.session_state.get("logged_in"):
#         if st.sidebar.button("Logout"):
#             st.session_state.clear()
#             st.rerun()
 
#     # --- RENDER PAGES ---
#     if st.session_state.page == "Login":
#         login_render()
#     elif st.session_state.page == "Sign Up":
#         signup_render()
#     elif st.session_state.page == "Symptom Checker":
#         symptom_render()
#     elif st.session_state.page == "Remedies":
#         remedy_render()
#     elif st.session_state.page == "Appointment":
#         appointment_render()
#     elif st.session_state.page == "Dashboard":
#         dashboard_render()
 
# if __name__ == "__main__":
#     home()
 
import streamlit as st
from views.login import render as login_render
from views.signup import render as signup_render
from views.symptom_checker import render as symptom_render
from views.remedies import render as remedy_render
from views.appointment import render as appointment_render
from views.feedback import render as dashboard_render 
# Function to load and inject the CSS file
def load_css():
    """Loads and injects a local CSS file and Google Fonts."""
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        st.markdown(
            """
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("`style.css` not found. Please create the file in the same directory.")
 
def home():
    """Main function to run the Streamlit application."""
    # This is the crucial line: call the function to load the CSS
    load_css()
 
    # --- SIDEBAR HEADER AND DYNAMIC CONTENT ---
    st.sidebar.markdown(
        """
        <div class="custom-logo">
            <h1>HealthMate</h1>
            <p>"HEALTH IS WEALTH"</p>
        </div>
        """,
        unsafe_allow_html=True
    )
 
    # Dynamic Welcome/Profile Section
    if st.session_state.get("logged_in") and "username" in st.session_state:
        st.sidebar.markdown(f"<div class='profile-info'>Hello, {st.session_state.username}!</div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
 
    # --- NAVIGATION ---
    if "page" not in st.session_state:
        st.session_state.page = "Login"
 
    page = st.sidebar.radio(
        "Go to",
        ["Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment", "Feedback"],
        index=["Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment", "Feedback"].index(st.session_state.page),
    )
 
    if page != st.session_state.page:
        st.session_state.page = page
        st.rerun()
 
    if st.session_state.get("logged_in"):
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.rerun()
 
    # --- RENDER PAGES ---
    if st.session_state.page == "Login":
        login_render()
    elif st.session_state.page == "Sign Up":
        signup_render()
    elif st.session_state.page == "Symptom Checker":
        symptom_render()
    elif st.session_state.page == "Remedies":
        remedy_render()
    elif st.session_state.page == "Appointment":
        appointment_render()
    elif st.session_state.page == "Feedback":
        dashboard_render()
 
if __name__ == "__main__":
    home()