# class Feedback:
#     def __init__(self, user_id, comment, rating):
#         self.user_id = user_id
#         self.comment = comment
#         self.rating = rating 

# class Feedback:
#     def __init__(self, user_id, comment, rating):
#         self.user_id = user_id
#         self.comment = comment
#         self.rating = rating


# feedback_model.py
from database import get_connection
import traceback

def save_feedback_to_db(patient_id, patient_name, doctor_id, doctor_name, rating, comment):
    """Save feedback to database"""
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                """INSERT INTO feedback (patient_id, patient_name, doctor_id, doctor_name, rating, comment) 
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (patient_id, patient_name, doctor_id, doctor_name, rating, comment)
            )
            conn.commit()
            return True
    except Exception as e:
        print(f"Error saving feedback: {e}")
        traceback.print_exc()
        return False
    finally:
        if conn:
            conn.close()

def get_feedback_for_doctor(doctor_id):
    """Get all feedback for a specific doctor"""
    try:
        conn = get_connection()
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(
                """SELECT * FROM feedback 
                WHERE doctor_id = %s 
                ORDER BY created_at DESC""",
                (doctor_id,)
            )
            feedback_list = cursor.fetchall()
            return feedback_list
    except Exception as e:
        print(f"Error fetching feedback: {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_feedback_by_patient(patient_id):
    """Get feedback given by a specific patient"""
    try:
        conn = get_connection()
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(
                """SELECT * FROM feedback 
                WHERE patient_id = %s 
                ORDER BY created_at DESC""",
                (patient_id,)
            )
            feedback_list = cursor.fetchall()
            return feedback_list
    except Exception as e:
        print(f"Error fetching patient feedback: {e}")
        return []
    finally:
        if conn:
            conn.close()
