# import streamlit as st
# import time

# # Set page config to update browser tab and sidebar label
# st.set_page_config(page_title="Feedback", page_icon="💬", layout="centered")

# # Feedback model class
# class Feedback:
#     def __init__(self, user_id, comment, rating):
#         self.user_id = user_id
#         self.comment = comment
#         self.rating = rating

# # Feedback submission controller
# def submit_feedback(feedback):
#     try:
#         # Simulate database/API logic
#         print(f"SUBMITTING TO DB: User ID: {feedback.user_id}, Comment: '{feedback.comment}', Rating: {feedback.rating}")
#         return True
#     except Exception as e:
#         print(f"Error submitting feedback for user {feedback.user_id}: {e}")
#         return False

# def render():
#     # Updated heading
#     st.markdown("<h1 style='text-align: center; color: #2e7d32;'>Feedback</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center; color: #4CAF50;'>We'd love to hear your thoughts and improve your experience!</p>", unsafe_allow_html=True)
    
#     comment = st.text_area("Your feedback", placeholder="Type your thoughts here...", height=150)
#     rating = st.slider("Rate your experience", min_value=1, max_value=5, value=5, key="feedback_rating")
    
#     # Submit button
#     if st.button("Submit Feedback"):
#         # Display a spinner to indicate that the submission is in progress
#         with st.spinner('Submitting feedback...'):
#             user_id = 1  # Replace with actual user ID from session/auth
            
#             # Create Feedback object
#             feedback = Feedback(user_id, comment, rating)
            
#             # Submit using controller
#             success = submit_feedback(feedback)
        
#         # Check the result after the spinner is finished
#         if success:
#             st.success("Thank you for your feedback!")
#         else:
#             st.error("Oops! Something went wrong. Please try again.")

# # Run the render function to display the app
# if __name__ == "__main__":
#     render()


# feedback.py
# import streamlit as st
# from controllers.feedback_controller import submit_feedback, get_patient_feedback
# from models.doctor_model import get_doctor_by_username

# def render():
#     st.set_page_config(page_title="Feedback", page_icon="💬", layout="centered")

#     if not st.session_state.get("logged_in"):
#         st.warning("Please log in first.")
#         return

#     st.markdown("<h1 style='text-align: center; color: #2e7d32;'>💬 Doctor Feedback</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center; color: #4CAF50;'>Share your experience with our doctors!</p>", unsafe_allow_html=True)
    
#     # Feedback form
#     with st.form("feedback_form"):
#         # Doctor selection
#         doctor_username = st.text_input("Doctor's Username", placeholder="Enter the doctor's username")
#         rating = st.slider("Rate your experience", min_value=1, max_value=5, value=5, 
#                           help="1 = Poor, 5 = Excellent")
#         comment = st.text_area("Your feedback", placeholder="Share your experience with the doctor...", height=150)
        
#         submitted = st.form_submit_button("📤 Submit Feedback")
    
#     if submitted:
#         if not doctor_username:
#             st.error("❌ Please enter the doctor's username")
#             return
            
#         if not comment.strip():
#             st.error("❌ Please enter your feedback")
#             return
        
#         # Verify doctor exists
#         doctor = get_doctor_by_username(doctor_username)
#         if not doctor:
#             st.error("❌ Doctor not found. Please check the username.")
#             return
        
#         with st.spinner('Submitting feedback...'):
#             success = submit_feedback(
#                 st.session_state["username"],
#                 doctor_username,
#                 rating,
#                 comment
#             )
        
#         if success:
#             st.success("✅ Thank you for your feedback! The doctor will see your review.")
#             st.rerun()
#         else:
#             st.error("❌ Failed to submit feedback. Please try again.")

#     # Show patient's previous feedback
#     st.markdown("---")
#     st.subheader("📋 Your Previous Feedback")
    
#     patient_feedback = get_patient_feedback(st.session_state["username"])
    
#     if not patient_feedback:
#         st.info("You haven't submitted any feedback yet.")
#     else:
#         for feedback in patient_feedback:
#             with st.expander(f"Feedback for Dr. {feedback['doctor_name']} - ⭐{feedback['rating']}/5"):
#                 st.write(f"**Rating:** {feedback['rating']}/5")
#                 st.write(f"**Comment:** {feedback['comment']}")
#                 st.write(f"**Submitted on:** {feedback['created_at']}")

# if __name__ == "__main__":
#     render()


# import streamlit as st
# from controllers.feedback_controller import submit_feedback, get_patient_feedback
# from models.doctor_model import get_all_doctors

# def render():
#     st.set_page_config(page_title="Feedback", page_icon="💬", layout="centered")

#     if not st.session_state.get("logged_in"):
#         st.warning("⚠️ Please log in first.")
#         return

#     st.markdown("<h1 style='text-align: center; color: #2e7d32;'>💬 Doctor Feedback</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center; color: #4CAF50;'>Share your experience with our doctors!</p>", unsafe_allow_html=True)
    
#     # Fetch all doctors from database
#     doctors = get_all_doctors()
    
#     if not doctors:
#         st.error("❌ No doctors available in the system. Please contact support.")
#         return
    
#     # Create a mapping for doctor selection
#     doctor_map = {}
#     doctor_display_list = []
    
#     for doc in doctors:
#         # Create display name with name and specialization
#         if 'specialization' in doc and doc['specialization']:
#             display_name = f"Dr. {doc['name']} - {doc['specialization']}"
#         else:
#             display_name = f"Dr. {doc['name']}"
        
#         doctor_display_list.append(display_name)
#         doctor_map[display_name] = doc['username']
    
#     # Feedback form
#     st.markdown("### 📝 Submit New Feedback")
#     with st.form("feedback_form", clear_on_submit=True):
#         # Doctor selection dropdown
#         selected_doctor_display = st.selectbox(
#             "Select Doctor *",
#             options=doctor_display_list,
#             help="Choose the doctor you want to give feedback to",
#             index=0
#         )
        
#         # Display selected doctor info
#         selected_doctor = next((d for d in doctors if doctor_map[selected_doctor_display] == d['username']), None)
#         if selected_doctor:
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.caption(f"👤 **Username:** {selected_doctor['username']}")
#             with col2:
#                 if 'email' in selected_doctor and selected_doctor['email']:
#                     st.caption(f"📧 **Email:** {selected_doctor['email']}")
        
#         st.markdown("---")
        
#         # Rating
#         rating = st.slider(
#             "Rate your experience *", 
#             min_value=1, 
#             max_value=5, 
#             value=5,
#             format="⭐ %d",
#             help="1 = Poor, 5 = Excellent"
#         )
        
#         # Show rating description
#         rating_descriptions = {
#             1: "😞 Poor - Very dissatisfied",
#             2: "😕 Below Average - Dissatisfied", 
#             3: "😐 Average - Neutral",
#             4: "😊 Good - Satisfied",
#             5: "😄 Excellent - Very satisfied"
#         }
#         st.info(rating_descriptions[rating])
        
#         # Comment
#         comment = st.text_area(
#             "Your feedback *", 
#             placeholder="Please share your experience with the doctor. Be specific about what went well or what could be improved...", 
#             height=150,
#             max_chars=500
#         )
        
#         st.caption("* Required fields")
        
#         # Submit button
#         col1, col2, col3 = st.columns([1, 1, 1])
#         with col2:
#             submitted = st.form_submit_button("📤 Submit Feedback", use_container_width=True)
    
#     if submitted:
#         # Validation
#         if not comment.strip():
#             st.error("❌ Please enter your feedback before submitting.")
#             return
        
#         if len(comment.strip()) < 10:
#             st.error("❌ Please provide more detailed feedback (at least 10 characters).")
#             return
        
#         # Get the username from the selected display name
#         doctor_username = doctor_map[selected_doctor_display]
        
#         with st.spinner('Submitting feedback...'):
#             success = submit_feedback(
#                 st.session_state["username"],
#                 doctor_username,
#                 rating,
#                 comment.strip()
#             )
        
#         if success:
#             st.success("✅ Thank you for your feedback! The doctor will see your review.")
#             st.balloons()
#             # Small delay before rerun
#             import time
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.error("❌ Failed to submit feedback. Please try again later.")

#     # Show patient's previous feedback
#     st.markdown("---")
#     st.markdown("### 📋 Your Previous Feedback")
    
#     patient_feedback = get_patient_feedback(st.session_state["username"])
    
#     if not patient_feedback:
#         st.info("💭 You haven't submitted any feedback yet. Be the first to share your experience!")
#     else:
#         st.caption(f"Total feedback submitted: {len(patient_feedback)}")
        
#         for idx, feedback in enumerate(patient_feedback):
#             # Create expander with colored rating
#             stars = "⭐" * feedback['rating']
#             with st.expander(f"**Dr. {feedback['doctor_name']}** | {stars} ({feedback['rating']}/5)", expanded=(idx == 0)):
#                 # Display feedback details
#                 col1, col2 = st.columns([2, 1])
                
#                 with col1:
#                     st.markdown(f"**👤 Doctor:** Dr. {feedback['doctor_name']}")
#                     st.markdown(f"**⭐ Rating:** {stars} ({feedback['rating']}/5)")
                
#                 with col2:
#                     st.markdown(f"**📅 Date:** {feedback['created_at'].strftime('%Y-%m-%d')}")
#                     st.markdown(f"**🕒 Time:** {feedback['created_at'].strftime('%H:%M')}")
                
#                 st.markdown("---")
#                 st.markdown("**💬 Your Comment:**")
#                 st.markdown(f"> {feedback['comment']}")

# if __name__ == "__main__":
#     render()


# feedback.py
import streamlit as st
from controllers.feedback_controller import submit_feedback, get_patient_feedback
from models.doctor_model import get_all_doctors
import time

def render():
    st.set_page_config(page_title="Feedback", page_icon="💬", layout="centered")

    # Check if user is logged in
    if not st.session_state.get("logged_in"):
        st.warning("⚠️ Please log in first.")
        st.stop()
        return

    # Check if username exists in session
    if not st.session_state.get("username"):
        st.error("❌ Session error: Username not found. Please log in again.")
        st.stop()
        return

    st.markdown("<h1 style='text-align: center; color: #2e7d32;'>💬 Doctor Feedback</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4CAF50;'>Share your experience with our doctors!</p>", unsafe_allow_html=True)
    
    # Fetch all doctors from database
    try:
        doctors = get_all_doctors()
    except Exception as e:
        st.error(f"❌ Error loading doctors: {str(e)}")
        return
    
    if not doctors or len(doctors) == 0:
        st.error("❌ No doctors available in the system. Please contact support.")
        return
    
    # Create a mapping for doctor selection
    doctor_map = {}
    doctor_display_list = []
    
    for doc in doctors:
        # Safely get doctor information
        doctor_name = doc.get('name', doc.get('username', 'Unknown'))
        doctor_username = doc.get('username', '')
        
        if not doctor_username:
            continue  # Skip doctors without username
        
        # Create display name with name and specialization
        specialization = doc.get('specialization', '')
        if specialization:
            display_name = f"Dr. {doctor_name} - {specialization}"
        else:
            display_name = f"Dr. {doctor_name}"
        
        doctor_display_list.append(display_name)
        doctor_map[display_name] = doctor_username
    
    if not doctor_display_list:
        st.error("❌ No valid doctors found in the system.")
        return
    
    # Feedback form
    st.markdown("### 📝 Submit New Feedback")
    with st.form("feedback_form", clear_on_submit=True):
        # Doctor selection dropdown
        selected_doctor_display = st.selectbox(
            "Select Doctor *",
            options=doctor_display_list,
            help="Choose the doctor you want to give feedback to",
            index=0
        )
        
        # Display selected doctor info
        selected_doctor = next(
            (d for d in doctors if doctor_map.get(selected_doctor_display) == d.get('username')), 
            None
        )
        
        if selected_doctor:
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"👤 **Username:** {selected_doctor.get('username', 'N/A')}")
            with col2:
                email = selected_doctor.get('email', '')
                if email:
                    st.caption(f"📧 **Email:** {email}")
        
        st.markdown("---")
        
        # Rating
        rating = st.slider(
            "Rate your experience *", 
            min_value=1, 
            max_value=5, 
            value=5,
            format="⭐ %d",
            help="1 = Poor, 5 = Excellent"
        )
        
        # Show rating description
        rating_descriptions = {
            1: "😞 Poor - Very dissatisfied",
            2: "😕 Below Average - Dissatisfied", 
            3: "😐 Average - Neutral",
            4: "😊 Good - Satisfied",
            5: "😄 Excellent - Very satisfied"
        }
        st.info(rating_descriptions[rating])
        
        # Comment
        comment = st.text_area(
            "Your feedback *", 
            placeholder="Please share your experience with the doctor. Be specific about what went well or what could be improved...", 
            height=150,
            max_chars=500,
            help="Minimum 10 characters required"
        )
        
        st.caption("* Required fields")
        
        # Submit button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submitted = st.form_submit_button("📤 Submit Feedback", use_container_width=True)
    
    if submitted:
        # Validation
        if not comment or not comment.strip():
            st.error("❌ Please enter your feedback before submitting.")
            st.stop()
        
        if len(comment.strip()) < 10:
            st.error("❌ Please provide more detailed feedback (at least 10 characters).")
            st.stop()
        
        # Get the username from the selected display name
        doctor_username = doctor_map.get(selected_doctor_display)
        
        if not doctor_username:
            st.error("❌ Error: Could not find doctor username. Please try again.")
            st.stop()
        
        with st.spinner('Submitting feedback...'):
            try:
                success = submit_feedback(
                    patient_username=st.session_state["username"],
                    doctor_username=doctor_username,
                    rating=rating,
                    comment=comment.strip()
                )
            except Exception as e:
                st.error(f"❌ Error submitting feedback: {str(e)}")
                success = False
        
        if success:
            st.success("✅ Thank you for your feedback! The doctor will see your review.")
            st.balloons()
            time.sleep(1.5)
            st.rerun()
        else:
            st.error("❌ Failed to submit feedback. Please try again later.")

    # Show patient's previous feedback
    st.markdown("---")
    st.markdown("### 📋 Your Previous Feedback")
    
    try:
        patient_feedback = get_patient_feedback(st.session_state["username"])
    except Exception as e:
        st.error(f"❌ Error loading your feedback: {str(e)}")
        patient_feedback = []
    
    if not patient_feedback or len(patient_feedback) == 0:
        st.info("💭 You haven't submitted any feedback yet. Be the first to share your experience!")
    else:
        st.caption(f"Total feedback submitted: {len(patient_feedback)}")
        
        for idx, feedback in enumerate(patient_feedback):
            # Safely get feedback data
            fb_rating = feedback.get('rating', 0)
            fb_doctor_name = feedback.get('doctor_name', 'Unknown')
            fb_comment = feedback.get('comment', '')
            fb_created_at = feedback.get('created_at')
            
            # Create expander with colored rating
            stars = "⭐" * fb_rating
            with st.expander(
                f"**Dr. {fb_doctor_name}** | {stars} ({fb_rating}/5)", 
                expanded=(idx == 0)
            ):
                # Display feedback details
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**👤 Doctor:** Dr. {fb_doctor_name}")
                    st.markdown(f"**⭐ Rating:** {stars} ({fb_rating}/5)")
                
                with col2:
                    if fb_created_at:
                        try:
                            st.markdown(f"**📅 Date:** {fb_created_at.strftime('%Y-%m-%d')}")
                            st.markdown(f"**🕒 Time:** {fb_created_at.strftime('%H:%M')}")
                        except:
                            st.markdown(f"**📅 Date:** {str(fb_created_at)}")
                
                st.markdown("---")
                st.markdown("**💬 Your Comment:**")
                st.markdown(f"> {fb_comment}")

if __name__ == "__main__":
    render()