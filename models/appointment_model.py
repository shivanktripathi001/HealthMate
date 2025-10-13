from database import get_connection

def get_hospitals():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hospitals")
        hospitals = cursor.fetchall()
        conn.close()
        return hospitals
    except Exception as e:
        print(f"Error fetching hospitals: {e}")
        return []

def create_appointment(user_id, hospital_id, symptom_id, date_time):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO appointments (user_id, hospital_id, symptom_id, date_time)
            VALUES (?, ?, ?, ?)
        """, (user_id, hospital_id, symptom_id, date_time))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating appointment: {e}")

def get_user_appointments(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.date_time, h.name, s.name
            FROM appointments a
            JOIN hospitals h ON a.hospital_id = h.hospital_id
            JOIN symptoms s ON a.symptom_id = s.symptom_id
            WHERE a.user_id = ?
        """, (user_id,))
        appointments = cursor.fetchall()
        conn.close()
        return appointments
    except Exception as e:
        print(f"Error fetching appointments: {e}")
        return []
