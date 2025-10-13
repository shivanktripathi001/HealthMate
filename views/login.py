# import streamlit as st
# from controllers.auth_controller import handle_login

# def render():
#     st.title("Login")

#     with st.form("login_form"):
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         submitted = st.form_submit_button("Login")

#         if submitted:
#             if handle_login(username, password):
#                 st.success("Login successful!")
#                 st.rerun()





# # views/login.py
# import streamlit as st
# from controllers.auth_controller import handle_login
# def render():
#     # Use a custom HTML container for better styling with CSS
#     st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    
#     st.markdown("<h1>Login to HealthMate</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center;'>Welcome back! Please enter your credentials.</p>", unsafe_allow_html=True)
    
#     # Use a Streamlit form to group inputs and the button
#     with st.form("login_form"):
#          username = st.text_input("Username", key="username_input")
#          password = st.text_input("Password", type="password", key="password_input")
        
#          # The submit button for the form
#          submitted = st.form_submit_button("Login")
    
#      # Handle the form submission and display feedback
#     if submitted:
#          if handle_login(username, password):
#              st.success("Login successful! Redirecting...")
#              # Store the username and login status in the session state
#              st.session_state.logged_in = True
#              st.session_state.username = username  # This is the added line
#              st.session_state.page = "Feedback"
#              st.rerun()
#          else:
#              st.error("Invalid username or password. Please try again.")
 
#      # A link to the sign-up page for new users
#     st.markdown(
#          "<p style='text-align: center; margin-top: 20px;'>Don't have an account? <a href='#'>Sign up here</a></p>",
#          unsafe_allow_html=True
#      )
    
#      # Close the custom HTML container
#     st.markdown("</div>", unsafe_allow_html=True)



# views/login.py
import streamlit as st
from controllers.auth_controller import handle_login
import time

def render():
    # Use a custom HTML container for better styling with CSS
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    
    st.markdown("<h1>Login to HealthMate</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Welcome back! Please enter your credentials.</p>", unsafe_allow_html=True)
    
    # Use a Streamlit form to group inputs and the button
    with st.form("login_form"):
        username = st.text_input("Username", key="username_input")
        password = st.text_input("Password", type="password", key="password_input")
        
        # The submit button for the form
        submitted = st.form_submit_button("Login")
    
    # Handle the form submission and display feedback
    if submitted:
        if handle_login(username, password):
            # Display success popup box
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
                    <h2 style="color: #333; margin-bottom: 10px;">Success!</h2>
                    <p style="color: #666; font-size: 16px;">You have successfully logged in</p>
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
            
            # Store the username and login status in the session state
            st.session_state.logged_in = True
            st.session_state.username = username
            
            # Small delay to show the success message
            time.sleep(2)
            
            st.session_state.page = "Feedback"
            st.rerun()
        else:
            st.error("Invalid username or password. Please try again.")
 
    # A link to the sign-up page for new users
    st.markdown(
        "<p style='text-align: center; margin-top: 20px;'>Don't have an account? <a href='#'>Sign up here</a></p>",
        unsafe_allow_html=True
    )
    
    # Close the custom HTML container
    st.markdown("</div>", unsafe_allow_html=True)

