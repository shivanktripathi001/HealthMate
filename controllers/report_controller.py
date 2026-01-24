# from models.report_model import create_report, get_reports_by_user
# from models.user_model import get_user_by_username
 
# def save_report(username, patient_name, age, diagnosis, prescription, notes):
#     user = get_user_by_username(username)
#     if not user:
#         return False
#     user_id = user["user_id"]
#     return create_report(user_id, patient_name, age, diagnosis, prescription, notes)
 
# def fetch_reports(username):
#     user = get_user_by_username(username)
#     if not user:
#         return []
#     user_id = user["user_id"]
#     return get_reports_by_user(user_id)

# report_controller.py
# from models.report_model import create_report, get_reports_by_user
# from models.user_model import get_user_by_username
# import traceback

# def save_report(username, patient_name, age, diagnosis, prescription, notes):
#     try:
#         print(f"Attempting to save report for user: {username}")
#         user = get_user_by_username(username)
#         print(f"User found: {user}")
        
#         if not user:
#             return False
        
#         # Use 'username' as user_id directly since your table uses username as foreign key
#         user_id = username  # This should match the user_id in your reports table
        
#         print(f"Creating report with user_id: {user_id}")
#         return create_report(user_id, patient_name, age, diagnosis, prescription, notes)
#     except Exception as e:
#         print(f"Error in save_report: {e}")
#         print(traceback.format_exc())
#         return False

# def fetch_reports(username):
#     try:
#         user = get_user_by_username(username)
#         if not user:
#             return []
        
#         # Use 'username' as user_id directly
#         user_id = username
#         return get_reports_by_user(user_id)
#     except Exception as e:
#         print(f"Error in fetch_reports: {e}")
#         return []


# report_controller.py
from models.report_model import create_report, get_reports_by_user
from models.user_model import get_user_by_username
import traceback

def save_report(username, patient_name, age, diagnosis, prescription, notes):
    try:
        print(f"Attempting to save report for user: {username}")
        user = get_user_by_username(username)
        print(f"User found: {user}")
        
        if not user:
            print("User not found!")
            return False
        
        # Get the actual user_id from the user object
        # Adjust this based on your user table structure
        user_id = user.get('user_id') or user.get('id') or user.get('username')
        
        print(f"Creating report with user_id: {user_id}")
        result = create_report(user_id, patient_name, age, diagnosis, prescription, notes)
        print(f"Report creation result: {result}")
        return result
    except Exception as e:
        print(f"Error in save_report: {e}")
        print(traceback.format_exc())
        return False

def fetch_reports(username):
    try:
        print(f"Fetching reports for user: {username}")
        user = get_user_by_username(username)
        
        if not user:
            print("User not found!")
            return []
        
        # Get the actual user_id from the user object
        user_id = user.get('user_id') or user.get('id') or user.get('username')
        
        print(f"Fetching reports for user_id: {user_id}")
        reports = get_reports_by_user(user_id)
        print(f"Found {len(reports)} reports")
        return reports
    except Exception as e:
        print(f"Error in fetch_reports: {e}")
        print(traceback.format_exc())
        return []