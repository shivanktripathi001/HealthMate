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
 
# import streamlit as st
# from views.login import render as login_render
# from views.signup import render as signup_render
# from views.symptom_checker import render as symptom_render
# from views.remedies import render as remedy_render
# from views.appointment import render as appointment_render
# from views.feedback import render as dashboard_render 
# # Function to load and inject the CSS file
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
#     # This is the crucial line: call the function to load the CSS
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
#         ["Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment", "Feedback"],
#         index=["Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment", "Feedback"].index(st.session_state.page),
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
#     elif st.session_state.page == "Feedback":
#         dashboard_render()
 
# if __name__ == "__main__":
#     home() 
# 
# 
# 
# import streamlit as st
# from views.login import render as login_render
# from views.signup import render as signup_render
# from views.symptom_checker import render as symptom_render
# from views.remedies import render as remedy_render
# from views.appointment import render as appointment_render
# from views.feedback import render as dashboard_render
# from views.doctor_login import render as doctor_login_render
# from views.doctor_dashboard import render as doctor_dashboard_render

# # Function to load and inject the CSS file
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
#     # This is the crucial line: call the function to load the CSS
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
#         st.sidebar.markdown(f"<div class='profile-info'>👤 Hello, {st.session_state.username}!</div>", unsafe_allow_html=True)
#     elif st.session_state.get("doctor_logged_in") and "doctor_name" in st.session_state:
#         st.sidebar.markdown(f"<div class='profile-info'>👨‍⚕️ Dr. {st.session_state.doctor_name}</div>", unsafe_allow_html=True)
#         st.sidebar.markdown(f"<div class='profile-info' style='font-size: 0.9em;'>🏥 {st.session_state.get('doctor_specialization', 'Specialist')}</div>", unsafe_allow_html=True)
    
#     st.sidebar.markdown("---")
 
#     # --- NAVIGATION ---
#     if "page" not in st.session_state:
#         st.session_state.page = "Login"
 
#     # Different navigation based on user type
#     if st.session_state.get("doctor_logged_in"):
#         # Doctor Navigation
#         page = st.sidebar.radio(
#             "🩺 Doctor Panel",
#             ["Doctor Dashboard"],
#             index=0
#         )
#     else:
#         # Regular User Navigation
#         pages = ["Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment", "Feedback", "Doctor Login","Reports"]
        
#         # Find current page index safely
#         try:
#             current_index = pages.index(st.session_state.page)
#         except ValueError:
#             current_index = 0
#             st.session_state.page = "Login"
        
#         page = st.sidebar.radio(
#             "📍 Navigation",
#             pages,
#             index=current_index,
#         )
 
#     if page != st.session_state.page:
#         st.session_state.page = page
#         st.rerun()
 
#     # Logout button for both user types
#     if st.session_state.get("logged_in") or st.session_state.get("doctor_logged_in"):
#         st.sidebar.markdown("---")
#         if st.sidebar.button("🚪 Logout", use_container_width=True):
#             # Clear session but preserve page structure
#             is_doctor = st.session_state.get("doctor_logged_in", False)
#             st.session_state.clear()
#             st.session_state.page = "Doctor Login" if is_doctor else "Login"
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
#     elif st.session_state.page == "Feedback":
#         dashboard_render()
#     elif st.session_state.page == "Doctor Login":
#         doctor_login_render()
#     elif st.session_state.page == "Doctor Dashboard":
#         doctor_dashboard_render()
#     elif st.session_state.page == "Reports":
#         report_render()
 
# if __name__ == "__main__":
#     home()   
# 
# 
import streamlit as st
from views.login import render as login_render
from views.signup import render as signup_render
from views.symptom_checker import render as symptom_render
from views.remedies import render as remedy_render
from views.appointment import render as appointment_render
from views.feedback import render as dashboard_render
from views.doctor_login import render as doctor_login_render
from views.doctor_dashboard import render as doctor_dashboard_render
from views.report import render as report_render  # Added this import

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
        st.sidebar.markdown(f"<div class='profile-info'>👤 Hello, {st.session_state.username}!</div>", unsafe_allow_html=True)
    elif st.session_state.get("doctor_logged_in") and "doctor_name" in st.session_state:
        st.sidebar.markdown(f"<div class='profile-info'>👨‍⚕️ Dr. {st.session_state.doctor_name}</div>", unsafe_allow_html=True)
        st.sidebar.markdown(f"<div class='profile-info' style='font-size: 0.9em;'>🏥 {st.session_state.get('doctor_specialization', 'Specialist')}</div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
 
    # --- NAVIGATION ---
    if "page" not in st.session_state:
        st.session_state.page = "Login"
 
    # Different navigation based on user type
    if st.session_state.get("doctor_logged_in"):
        # Doctor Navigation
        page = st.sidebar.radio(
            "🩺 Doctor Panel",
            ["Doctor Dashboard"],
            index=0
        )
    else:
        # Regular User Navigation
        pages = ["Login", "Sign Up", "Symptom Checker", "Remedies", "Appointment",  "Doctor Login", "Reports"]
        
        # Find current page index safely
        try:
            current_index = pages.index(st.session_state.page)
        except ValueError:
            current_index = 0
            st.session_state.page = "Login"
        
        page = st.sidebar.radio(
            "📋 Navigation",
            pages,
            index=current_index,
        )
 
    if page != st.session_state.page:
        st.session_state.page = page
        st.rerun()
 
    # Logout button for both user types
    if st.session_state.get("logged_in") or st.session_state.get("doctor_logged_in"):
        st.sidebar.markdown("---")
        if st.sidebar.button("🚪 Logout", use_container_width=True):
            # Clear session but preserve page structure
            is_doctor = st.session_state.get("doctor_logged_in", False)
            st.session_state.clear()
            st.session_state.page = "Doctor Login" if is_doctor else "Login"
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
    elif st.session_state.page == "Doctor Login":
        doctor_login_render()
    elif st.session_state.page == "Doctor Dashboard":
        doctor_dashboard_render()
    elif st.session_state.page == "Reports":
        report_render()  # Now this will work
 
if __name__ == "__main__":
    home()              