# import streamlit as st
# from controllers.auth_controller import handle_signup

# def render():
#     st.title("Sign Up")

#     with st.form("signup_form"):
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         email = st.text_input("Email")
#         submitted = st.form_submit_button("Sign Up")

#         if submitted:
#             if handle_signup(username, password, email):
#                 st.success("Account created successfully!")
#                 st.experimental_rerun()



import streamlit as st
from controllers.auth_controller import handle_signup
 
def render():
    # Use a custom HTML container for styling, consistent with the login page
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
 
    st.markdown("<h1>Join HealthMate</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Create an account to get started on your wellness journey.</p>", unsafe_allow_html=True)
 
    with st.form("signup_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Sign Up")
        
    if submitted:
        if handle_signup(username, password, email):
            st.success("Account created successfully! You can now log in.")
            # Use st.rerun() to refresh the page after successful signup
            st.rerun()
        else:
            st.error("Failed to create account. This username or email might already be taken.")
 
    # A link to the login page for existing users
    st.markdown(
        "<p style='text-align: center; margin-top: 20px;'>Already have an account? <a href='#'>Log in here</a></p>",
        unsafe_allow_html=True
    )
    
    # Close the custom HTML container
    st.markdown("</div>", unsafe_allow_html=True)
 