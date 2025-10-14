# models/doctor_model.py
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="healthmate_schema",
        cursorclass=pymysql.cursors.DictCursor
    )

def get_doctor_by_username(username):
    """Fetch doctor by username"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM doctors WHERE username = %s", (username,))
        doctor = cursor.fetchone()
        return doctor
    except Exception as e:
        print(f"Error fetching doctor: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_all_appointments_for_hospital(hospital_id):
    """Fetch all appointments for a specific hospital"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        query = """
            SELECT 
                a.appointment_id,
                a.appointment_date,
                a.status,
                u.username as patient_name,
                u.email as patient_email,
                s.symptom_name,
                s.description as symptom_description,
                h.name as hospital_name
            FROM appointments a
            JOIN users u ON a.user_id = u.user_id
            JOIN symptoms s ON a.symptom_id = s.symptom_id
            JOIN hospitals h ON a.hospital_id = h.hospital_id
            WHERE a.hospital_id = %s
            ORDER BY a.appointment_date DESC
        """
        cursor.execute(query, (hospital_id,))
        appointments = cursor.fetchall()
        return appointments
    except Exception as e:
        print(f"Error fetching appointments: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def update_appointment_status(appointment_id, status):
    """Update appointment status"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "UPDATE appointments SET status = %s WHERE appointment_id = %s",
            (status, appointment_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating appointment status: {e}")
        return False
    finally:
        cursor.close()
        conn.close()