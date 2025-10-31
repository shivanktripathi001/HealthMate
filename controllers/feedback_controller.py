# def submit_feedback(user_id, comment, rating):
#     try:
#         # 1. Connect to database/API
#         # 2. Insert data (user_id, comment, rating)
#         # 3. Commit transaction
        
#         # If all steps above are successful
#         return True
        
#     except Exception as e:
#         # Log the error for debugging
#         print(f"Error submitting feedback for user {user_id}: {e}")
#         # Return False to signal failure to the Streamlit app
#         return False

# def submit_feedback(user_id, comment, rating):
#     try:
#         # 1. Connect to database/API
#         # 2. Insert data (user_id, comment, rating)
#         # 3. Commit transaction
        
#         # If all steps above are successful
#         return True
        
#     except Exception as e:
#         # Log the error for debugging
#         print(f"Error submitting feedback for user {user_id}: {e}")
#         # Return False to signal failure to the Streamlit app
#         return False
    


    # feedback_controller.py
from models.feedback_model import save_feedback_to_db, get_feedback_for_doctor, get_feedback_by_patient
from models.doctor_model import get_doctor_by_username
from models.user_model import get_user_by_username
import traceback

def submit_feedback(patient_username, doctor_username, rating, comment):
    """Submit feedback from patient to doctor"""
    try:
        # Get patient details
        patient = get_user_by_username(patient_username)
        if not patient:
            print(f"Patient not found: {patient_username}")
            return False
        
        # Get doctor details
        doctor = get_doctor_by_username(doctor_username)
        if not doctor:
            print(f"Doctor not found: {doctor_username}")
            return False
        
        # Save feedback to database
        success = save_feedback_to_db(
            patient_id=patient_username,
            patient_name=patient_username,  # or use patient['name'] if available
            doctor_id=doctor['doctor_id'],
            doctor_name=doctor['name'],
            rating=rating,
            comment=comment
        )
        
        return success
        
    except Exception as e:
        print(f"Error in submit_feedback: {e}")
        traceback.print_exc()
        return False

def get_doctor_feedback(doctor_id):
    """Get all feedback for a doctor"""
    try:
        return get_feedback_for_doctor(doctor_id)
    except Exception as e:
        print(f"Error getting doctor feedback: {e}")
        return []

def get_patient_feedback(patient_username):
    """Get feedback given by a patient"""
    try:
        return get_feedback_by_patient(patient_username)
    except Exception as e:
        print(f"Error getting patient feedback: {e}")
        return []