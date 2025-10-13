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

def submit_feedback(user_id, comment, rating):
    try:
        # 1. Connect to database/API
        # 2. Insert data (user_id, comment, rating)
        # 3. Commit transaction
        
        # If all steps above are successful
        return True
        
    except Exception as e:
        # Log the error for debugging
        print(f"Error submitting feedback for user {user_id}: {e}")
        # Return False to signal failure to the Streamlit app
        return False