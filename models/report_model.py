# from database import get_connection
 
# def create_report(user_id, patient_name, age, diagnosis, prescription, notes):
#     try:
#         conn = get_connection()
#         with conn.cursor() as cursor:
#             cursor.execute(
#                 "INSERT INTO reports (user_id, patient_name, age, diagnosis, prescription, notes) VALUES (%s, %s, %s, %s, %s, %s)",
#                 (user_id, patient_name, age, diagnosis, prescription, notes)
#             )
#         conn.commit()
#         return True
#     except Exception:
#         return False
 
# def get_reports_by_user(user_id):
#     try:
#         conn = get_connection()
#         with conn.cursor() as cursor:
#             cursor.execute("SELECT * FROM reports WHERE user_id = %s", (user_id,))
#             reports = cursor.fetchall()
#         return reports
#     except Exception:
#         return []


# report_model.py
# from database import get_connection
# import traceback

# def create_report(user_id, patient_name, age, diagnosis, prescription, notes):
#     try:
#         conn = get_connection()
#         with conn.cursor() as cursor:
#             cursor.execute(
#                 "INSERT INTO reports (user_id, patient_name, age, diagnosis, prescription, notes) VALUES (%s, %s, %s, %s, %s, %s)",
#                 (user_id, patient_name, age, diagnosis, prescription, notes)
#             )
#         conn.commit()
#         return True
#     except Exception as e:
#         print(f"Error creating report: {e}")
#         print(traceback.format_exc())
#         return False
#     finally:
#         if conn:
#             conn.close()

# def get_reports_by_user(user_id):
#     try:
#         conn = get_connection()
#         with conn.cursor(dictionary=True) as cursor:  # Add dictionary=True to get dict results
#             cursor.execute("SELECT * FROM reports WHERE user_id = %s ORDER BY created_at DESC", (user_id,))
#             reports = cursor.fetchall()
#         return reports
#     except Exception as e:
#         print(f"Error fetching reports: {e}")
#         return []
#     finally:
#         if conn:
#             conn.close()

# report_model.py
from database import get_connection
import traceback

def create_report(user_id, patient_name, age, diagnosis, prescription, notes):
    conn = None
    try:
        print(f"Connecting to database...")
        conn = get_connection()
        print(f"Connection established: {conn}")
        
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO reports 
                (user_id, patient_name, age, diagnosis, prescription, notes) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            print(f"Executing SQL: {sql}")
            print(f"Values: user_id={user_id}, patient_name={patient_name}, age={age}")
            
            cursor.execute(sql, (user_id, patient_name, age, diagnosis, prescription, notes))
            conn.commit()
            print(f"Report inserted successfully! Insert ID: {cursor.lastrowid}")
        return True
    except Exception as e:
        print(f"Error creating report: {e}")
        print(traceback.format_exc())
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            try:
                conn.close()
                print("Connection closed")
            except:
                pass

def get_reports_by_user(user_id):
    conn = None
    try:
        print(f"Fetching reports for user_id: {user_id}")
        conn = get_connection()
        
        with conn.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM reports WHERE user_id = %s ORDER BY created_at DESC"
            print(f"Executing SQL: {sql}")
            cursor.execute(sql, (user_id,))
            reports = cursor.fetchall()
            print(f"Found {len(reports)} reports")
        return reports
    except Exception as e:
        print(f"Error fetching reports: {e}")
        print(traceback.format_exc())
        return []
    finally:
        if conn:
            try:
                conn.close()
            except:
                pass