import streamlit as st
import time

# Set page config to update browser tab and sidebar label
st.set_page_config(page_title="Feedback", page_icon="💬", layout="centered")

# Feedback model class
class Feedback:
    def __init__(self, user_id, comment, rating):
        self.user_id = user_id
        self.comment = comment
        self.rating = rating

# Feedback submission controller
def submit_feedback(feedback):
    try:
        # Simulate database/API logic
        print(f"SUBMITTING TO DB: User ID: {feedback.user_id}, Comment: '{feedback.comment}', Rating: {feedback.rating}")
        return True
    except Exception as e:
        print(f"Error submitting feedback for user {feedback.user_id}: {e}")
        return False

def render():
    # Updated heading
    st.markdown("<h1 style='text-align: center; color: #2e7d32;'>Feedback</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4CAF50;'>We'd love to hear your thoughts and improve your experience!</p>", unsafe_allow_html=True)
    
    comment = st.text_area("Your feedback", placeholder="Type your thoughts here...", height=150)
    rating = st.slider("Rate your experience", min_value=1, max_value=5, value=5, key="feedback_rating")
    
    # Submit button
    if st.button("Submit Feedback"):
        # Display a spinner to indicate that the submission is in progress
        with st.spinner('Submitting feedback...'):
            user_id = 1  # Replace with actual user ID from session/auth
            
            # Create Feedback object
            feedback = Feedback(user_id, comment, rating)
            
            # Submit using controller
            success = submit_feedback(feedback)
        
        # Check the result after the spinner is finished
        if success:
            st.success("Thank you for your feedback!")
        else:
            st.error("Oops! Something went wrong. Please try again.")

# Run the render function to display the app
if __name__ == "__main__":
    render()
