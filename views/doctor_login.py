import streamlit as st
from controllers.doctor_controller import handle_doctor_login
import time

def render():
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    
    st.markdown("<h1>🩺 Doctor Login</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Access your admin panel</p>", unsafe_allow_html=True)
    
    with st.form("doctor_login_form"):
        username = st.text_input("Doctor Username", key="doctor_username")
        password = st.text_input("Password", type="password", key="doctor_password")
        
        submitted = st.form_submit_button("Login as Doctor")
    
    if submitted:
        if handle_doctor_login(username, password):
            st.markdown("""
                <div style="
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background-color: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    z-index: 9999;
                    min-width: 300px;
                ">
                    <div style="
                        width: 60px;
                        height: 60px;
                        background-color: #4CAF50;
                        border-radius: 50%;
                        margin: 0 auto 20px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    ">
                        <span style="color: white; font-size: 30px;">✓</span>
                    </div>
                    <h2 style="color: #333; margin-bottom: 10px;">Welcome Doctor!</h2>
                    <p style="color: #666; font-size: 16px;">Redirecting to admin panel...</p>
                </div>
                <div style="
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0, 0, 0, 0.5);
                    z-index: 9998;
                "></div>
            """, unsafe_allow_html=True)
            
            time.sleep(2)
            st.session_state.page = "Doctor Dashboard"
            st.rerun()
        else:
            st.error("Invalid credentials. Please try again.")
    
    st.markdown("</div>", unsafe_allow_html=True)