# # # # from database import get_connection

# # # # def get_hospitals():
# # # #     try:
# # # #         conn = get_connection()
# # # #         cursor = conn.cursor()
# # # #         cursor.execute("SELECT * FROM hospitals")
# # # #         hospitals = cursor.fetchall()
# # # #         conn.close()
# # # #         return hospitals
# # # #     except Exception as e:
# # # #         print(f"Error fetching hospitals: {e}")
# # # #         return []

# # # # def create_appointment(user_id, hospital_id, symptom_id, date_time):
# # # #     try:
# # # #         conn = get_connection()
# # # #         cursor = conn.cursor()
# # # #         cursor.execute("""
# # # #             INSERT INTO appointments (user_id, hospital_id, symptom_id, date_time)
# # # #             VALUES (?, ?, ?, ?)
# # # #         """, (user_id, hospital_id, symptom_id, date_time))
# # # #         conn.commit()
# # # #         conn.close()
# # # #     except Exception as e:
# # # #         print(f"Error creating appointment: {e}")

# # # # def get_user_appointments(user_id):
# # # #     try:
# # # #         conn = get_connection()
# # # #         cursor = conn.cursor()
# # # #         cursor.execute("""
# # # #             SELECT a.date_time, h.name, s.name
# # # #             FROM appointments a
# # # #             JOIN hospitals h ON a.hospital_id = h.hospital_id
# # # #             JOIN symptoms s ON a.symptom_id = s.symptom_id
# # # #             WHERE a.user_id = ?
# # # #         """, (user_id,))
# # # #         appointments = cursor.fetchall()
# # # #         conn.close()
# # # #         return appointments
# # # #     except Exception as e:
# # # #         print(f"Error fetching appointments: {e}")
# # # #         return []



# # # from database import get_connection
# # # import traceback

# # # def get_hospitals():
# # #     try:
# # #         conn = get_connection()
# # #         cursor = conn.cursor()
# # #         cursor.execute("SELECT * FROM hospitals")
# # #         hospitals = cursor.fetchall()
# # #         conn.close()
# # #         print(f"✓ Successfully fetched {len(hospitals)} hospitals")
# # #         return hospitals
# # #     except Exception as e:
# # #         print(f"✗ Error fetching hospitals: {e}")
# # #         traceback.print_exc()
# # #         return []

# # # def create_appointment(user_id, hospital_id, symptom_id, date_time):
# # #     try:
# # #         print(f"\n=== Creating Appointment ===")
# # #         print(f"User ID: {user_id}")
# # #         print(f"Hospital ID: {hospital_id}")
# # #         print(f"Symptom ID: {symptom_id}")
# # #         print(f"Date/Time: {date_time}")
        
# # #         conn = get_connection()
# # #         cursor = conn.cursor()
        
# # #         # Verify the appointment doesn't already exist
# # #         cursor.execute("""
# # #             SELECT COUNT(*) FROM appointments 
# # #             WHERE user_id = ? AND hospital_id = ? AND symptom_id = ? AND date_time = ?
# # #         """, (user_id, hospital_id, symptom_id, date_time))
        
# # #         existing = cursor.fetchone()[0]
# # #         if existing > 0:
# # #             print(f"⚠ Warning: Similar appointment already exists")
        
# # #         # Insert the appointment
# # #         cursor.execute("""
# # #             INSERT INTO appointments (user_id, hospital_id, symptom_id, date_time)
# # #             VALUES (?, ?, ?, ?)
# # #         """, (user_id, hospital_id, symptom_id, date_time))
        
# # #         # Get the inserted row ID
# # #         appointment_id = cursor.lastrowid
# # #         print(f"✓ Inserted appointment with ID: {appointment_id}")
        
# # #         # Commit the transaction
# # #         conn.commit()
# # #         print(f"✓ Transaction committed successfully")
        
# # #         # Verify the insert
# # #         cursor.execute("SELECT * FROM appointments WHERE appointment_id = ?", (appointment_id,))
# # #         inserted = cursor.fetchone()
# # #         print(f"✓ Verification: Row exists in DB: {inserted is not None}")
        
# # #         conn.close()
# # #         return True
        
# # #     except Exception as e:
# # #         print(f"✗ Error creating appointment: {e}")
# # #         traceback.print_exc()
# # #         if 'conn' in locals():
# # #             conn.rollback()
# # #             conn.close()
# # #         return False

# # # def get_user_appointments(user_id):
# # #     try:
# # #         conn = get_connection()
# # #         cursor = conn.cursor()
# # #         cursor.execute("""
# # #             SELECT a.appointment_id, a.date_time, h.name, s.name
# # #             FROM appointments a
# # #             JOIN hospitals h ON a.hospital_id = h.hospital_id
# # #             JOIN symptoms s ON a.symptom_id = s.symptom_id
# # #             WHERE a.user_id = ?
# # #             ORDER BY a.date_time DESC
# # #         """, (user_id,))
# # #         appointments = cursor.fetchall()
# # #         conn.close()
# # #         print(f"✓ Fetched {len(appointments)} appointments for user {user_id}")
# # #         return appointments
# # #     except Exception as e:
# # #         print(f"✗ Error fetching appointments: {e}")
# # #         traceback.print_exc()
# # #         return []






# # from database import get_connection
# # import traceback

# # def get_doctors():
# #     """Fetch all doctors with their hospital information"""
# #     try:
# #         conn = get_connection()
# #         cursor = conn.cursor()
# #         cursor.execute("""
# #             SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
# #                    h.city, d.contact, d.email
# #             FROM doctors d
# #             LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
# #             ORDER BY d.name
# #         """)
# #         doctors = cursor.fetchall()
# #         conn.close()
# #         print(f"✓ Successfully fetched {len(doctors)} doctors")
# #         return doctors
# #     except Exception as e:
# #         print(f"✗ Error fetching doctors: {e}")
# #         traceback.print_exc()
# #         return []

# # def get_doctors_by_specialization(specialization):
# #     """Fetch doctors filtered by specialization"""
# #     try:
# #         conn = get_connection()
# #         cursor = conn.cursor()
# #         cursor.execute("""
# #             SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
# #                    h.city, d.contact, d.email
# #             FROM doctors d
# #             LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
# #             WHERE d.specialization = ?
# #             ORDER BY d.name
# #         """, (specialization,))
# #         doctors = cursor.fetchall()
# #         conn.close()
# #         print(f"✓ Found {len(doctors)} doctors with specialization: {specialization}")
# #         return doctors
# #     except Exception as e:
# #         print(f"✗ Error fetching doctors by specialization: {e}")
# #         traceback.print_exc()
# #         return []

# # def get_all_specializations():
# #     """Get list of all unique specializations"""
# #     try:
# #         conn = get_connection()
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT DISTINCT specialization FROM doctors ORDER BY specialization")
# #         specializations = [row[0] for row in cursor.fetchall()]
# #         conn.close()
# #         return specializations
# #     except Exception as e:
# #         print(f"✗ Error fetching specializations: {e}")
# #         traceback.print_exc()
# #         return []

# # def create_appointment(user_id, doctor_id, symptom_id, date_time):
# #     """Create an appointment with a doctor"""
# #     try:
# #         print(f"\n=== Creating Appointment ===")
# #         print(f"User ID: {user_id}")
# #         print(f"Doctor ID: {doctor_id}")
# #         print(f"Symptom ID: {symptom_id}")
# #         print(f"Date/Time: {date_time}")
        
# #         conn = get_connection()
# #         cursor = conn.cursor()
        
# #         # Verify the appointment doesn't already exist
# #         cursor.execute("""
# #             SELECT COUNT(*) FROM appointments 
# #             WHERE user_id = ? AND doctor_id = ? AND date_time = ?
# #         """, (user_id, doctor_id, date_time))
        
# #         existing = cursor.fetchone()[0]
# #         if existing > 0:
# #             print(f"⚠ Warning: Similar appointment already exists")
# #             conn.close()
# #             return False
        
# #         # Insert the appointment
# #         cursor.execute("""
# #             INSERT INTO appointments (user_id, doctor_id, symptom_id, date_time)
# #             VALUES (?, ?, ?, ?)
# #         """, (user_id, doctor_id, symptom_id, date_time))
        
# #         # Get the inserted row ID
# #         appointment_id = cursor.lastrowid
# #         print(f"✓ Inserted appointment with ID: {appointment_id}")
        
# #         # Commit the transaction
# #         conn.commit()
# #         print(f"✓ Transaction committed successfully")
        
# #         # Verify the insert
# #         cursor.execute("SELECT * FROM appointments WHERE appointment_id = ?", (appointment_id,))
# #         inserted = cursor.fetchone()
# #         print(f"✓ Verification: Row exists in DB: {inserted is not None}")
        
# #         conn.close()
# #         return True
        
# #     except Exception as e:
# #         print(f"✗ Error creating appointment: {e}")
# #         traceback.print_exc()
# #         if 'conn' in locals():
# #             try:
# #                 conn.rollback()
# #                 conn.close()
# #             except:
# #                 pass
# #         return False

# # def get_user_appointments(user_id):
# #     """Fetch all appointments for a user"""
# #     try:
# #         conn = get_connection()
# #         cursor = conn.cursor()
# #         cursor.execute("""
# #             SELECT a.appointment_id, a.date_time, d.name as doctor_name, 
# #                    d.specialization, h.name as hospital_name, s.severity_level
# #             FROM appointments a
# #             JOIN doctors d ON a.doctor_id = d.doctor_id
# #             LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
# #             JOIN symptoms s ON a.symptom_id = s.symptom_id
# #             WHERE a.user_id = ?
# #             ORDER BY a.date_time DESC
# #         """, (user_id,))
# #         appointments = cursor.fetchall()
# #         conn.close()
# #         print(f"✓ Fetched {len(appointments)} appointments for user {user_id}")
# #         return appointments
# #     except Exception as e:
# #         print(f"✗ Error fetching appointments: {e}")
# #         traceback.print_exc()
# #         return []

# # def get_doctor_by_id(doctor_id):
# #     """Fetch a specific doctor's details"""
# #     try:
# #         conn = get_connection()
# #         cursor = conn.cursor()
# #         cursor.execute("""
# #             SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
# #                    h.city, d.contact, d.email
# #             FROM doctors d
# #             LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
# #             WHERE d.doctor_id = ?
# #         """, (doctor_id,))
# #         doctor = cursor.fetchone()
# #         conn.close()
# #         return doctor
# #     except Exception as e:
# #         print(f"✗ Error fetching doctor: {e}")
# #         traceback.print_exc()
# #         return None 



# from database import get_connection
# import traceback

# def get_doctors():
#     """Fetch all doctors with their hospital information"""
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
#                    h.city, d.contact, d.email
#             FROM doctors d
#             LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
#             ORDER BY d.name
#         """)
#         doctors = cursor.fetchall()
#         conn.close()
#         print(f"✓ Successfully fetched {len(doctors)} doctors")
        
#         # Convert to list of tuples if they're dicts
#         if doctors and isinstance(doctors[0], dict):
#             doctors = [(d['doctor_id'], d['name'], d['specialization'], 
#                        d.get('hospital_name'), d.get('city'), d.get('contact'), d.get('email')) 
#                        for d in doctors]
        
#         return doctors
#     except Exception as e:
#         print(f"✗ Error fetching doctors: {e}")
#         traceback.print_exc()
#         return []

# def get_doctors_by_specialization(specialization):
#     """Fetch doctors filtered by specialization"""
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
#                    h.city, d.contact, d.email
#             FROM doctors d
#             LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
#             WHERE d.specialization = %s
#             ORDER BY d.name
#         """, (specialization,))
#         doctors = cursor.fetchall()
#         conn.close()
#         print(f"✓ Found {len(doctors)} doctors with specialization: {specialization}")
#         return doctors
#     except Exception as e:
#         print(f"✗ Error fetching doctors by specialization: {e}")
#         traceback.print_exc()
#         return []

# def get_all_specializations():
#     """Get list of all unique specializations"""
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT DISTINCT specialization FROM doctors ORDER BY specialization")
#         specializations = [row[0] for row in cursor.fetchall()]
#         conn.close()
#         return specializations
#     except Exception as e:
#         print(f"✗ Error fetching specializations: {e}")
#         traceback.print_exc()
#         return []

# def create_appointment(user_id, doctor_id, symptom_id, date_time):
#     """Create an appointment with a doctor"""
#     try:
#         print(f"\n=== Creating Appointment ===")
#         print(f"User ID: {user_id} (type: {type(user_id)})")
#         print(f"Doctor ID: {doctor_id} (type: {type(doctor_id)})")
#         print(f"Symptom ID: {symptom_id} (type: {type(symptom_id)})")
#         print(f"Date/Time: {date_time} (type: {type(date_time)})")
        
#         conn = get_connection()
#         cursor = conn.cursor()
        
#         # Check if IDs exist
#         print("\n--- Checking if IDs exist ---")
#         cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
#         if not cursor.fetchone():
#             print(f"✗ User ID {user_id} does not exist!")
#             conn.close()
#             return False
#         print(f"✓ User ID {user_id} exists")
        
#         cursor.execute("SELECT doctor_id FROM doctors WHERE doctor_id = %s", (doctor_id,))
#         if not cursor.fetchone():
#             print(f"✗ Doctor ID {doctor_id} does not exist!")
#             conn.close()
#             return False
#         print(f"✓ Doctor ID {doctor_id} exists")
        
#         cursor.execute("SELECT symptom_id FROM symptoms WHERE symptom_id = %s", (symptom_id,))
#         if not cursor.fetchone():
#             print(f"✗ Symptom ID {symptom_id} does not exist!")
#             conn.close()
#             return False
#         print(f"✓ Symptom ID {symptom_id} exists")
        
#         # Verify the appointment doesn't already exist
#         print("\n--- Checking for duplicates ---")
#         cursor.execute("""
#             SELECT COUNT(*) FROM appointments 
#             WHERE user_id = %s AND doctor_id = %s AND date_time = %s
#         """, (user_id, doctor_id, date_time))
        
#         existing = cursor.fetchone()[0]
#         if existing > 0:
#             print(f"⚠ Warning: This exact appointment already exists!")
#             conn.close()
#             return False
#         print("✓ No duplicate found")
        
#         # Insert the appointment
#         print("\n--- Inserting appointment ---")
#         cursor.execute("""
#             INSERT INTO appointments (user_id, doctor_id, symptom_id, date_time)
#             VALUES (%s, %s, %s, %s)
#         """, (user_id, doctor_id, symptom_id, date_time))
        
#         # Get the inserted row ID
#         appointment_id = cursor.lastrowid
#         print(f"✓ Inserted appointment with ID: {appointment_id}")
        
#         # Commit the transaction
#         print("\n--- Committing transaction ---")
#         conn.commit()
#         print(f"✓ Transaction committed successfully")
        
#         # Verify the insert
#         print("\n--- Verifying insert ---")
#         cursor.execute("SELECT * FROM appointments WHERE appointment_id = %s", (appointment_id,))
#         inserted = cursor.fetchone()
        
#         if inserted:
#             print(f"✓ Verification successful: {inserted}")
#             conn.close()
#             return True
#         else:
#             print("✗ Verification failed: Row not found after commit!")
#             conn.close()
#             return False
        
#     except Exception as e:
#         print(f"\n✗ ERROR occurred:")
#         print(f"  Error type: {type(e).__name__}")
#         print(f"  Error message: {str(e)}")
#         print("\nFull traceback:")
#         traceback.print_exc()
        
#         if 'conn' in locals():
#             try:
#                 conn.rollback()
#                 print("\n✓ Transaction rolled back")
#                 conn.close()
#             except:
#                 pass
#         return False

# def get_user_appointments(user_id):
#     """Fetch all appointments for a user"""
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT a.appointment_id, a.date_time, d.name as doctor_name, 
#                    d.specialization, h.name as hospital_name, s.severity_level
#             FROM appointments a
#             JOIN doctors d ON a.doctor_id = d.doctor_id
#             LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
#             JOIN symptoms s ON a.symptom_id = s.symptom_id
#             WHERE a.user_id = %s
#             ORDER BY a.date_time DESC
#         """, (user_id,))
#         appointments = cursor.fetchall()
#         conn.close()
#         print(f"✓ Fetched {len(appointments)} appointments for user {user_id}")
#         return appointments
#     except Exception as e:
#         print(f"✗ Error fetching appointments: {e}")
#         traceback.print_exc()
#         return []

# def get_doctor_by_id(doctor_id):
#     """Fetch a specific doctor's details"""
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
#                    h.city, d.contact, d.email
#             FROM doctors d
#             LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
#             WHERE d.doctor_id = %s
#         """, (doctor_id,))
#         doctor = cursor.fetchone()
#         conn.close()
#         return doctor
#     except Exception as e:
#         print(f"✗ Error fetching doctor: {e}")
#         traceback.print_exc()
#         return None


from database import get_connection
import traceback

def safe_get_value(row, key_or_index):
    """Safely get value from row whether it's a dict or tuple"""
    if row is None:
        return None
    if isinstance(row, dict):
        return row.get(key_or_index)
    else:
        try:
            return row[key_or_index] if isinstance(key_or_index, int) else None
        except:
            return None

def get_doctors():
    """Fetch all doctors with their hospital information"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
                   h.city, d.contact, d.email
            FROM doctors d
            LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
            ORDER BY d.name
        """)
        doctors = cursor.fetchall()
        conn.close()
        print(f"✓ Successfully fetched {len(doctors)} doctors")
        return doctors
    except Exception as e:
        print(f"✗ Error fetching doctors: {e}")
        traceback.print_exc()
        return []

def get_doctors_by_specialization(specialization):
    """Fetch doctors filtered by specialization"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
                   h.city, d.contact, d.email
            FROM doctors d
            LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
            WHERE d.specialization = %s
            ORDER BY d.name
        """, (specialization,))
        doctors = cursor.fetchall()
        conn.close()
        print(f"✓ Found {len(doctors)} doctors with specialization: {specialization}")
        return doctors
    except Exception as e:
        print(f"✗ Error fetching doctors by specialization: {e}")
        traceback.print_exc()
        return []

def get_all_specializations():
    """Get list of all unique specializations"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT specialization FROM doctors WHERE specialization IS NOT NULL ORDER BY specialization")
        rows = cursor.fetchall()
        conn.close()
        
        # Handle both dict and tuple results
        if rows:
            if isinstance(rows[0], dict):
                specializations = [row['specialization'] for row in rows]
            else:
                specializations = [row[0] for row in rows]
            return specializations
        return []
    except Exception as e:
        print(f"✗ Error fetching specializations: {e}")
        traceback.print_exc()
        return []

def create_appointment(user_id, doctor_id, symptom_id, date_time):
    """Create an appointment with a doctor"""
    conn = None
    try:
        print(f"\n=== Creating Appointment ===")
        print(f"User ID: {user_id} (type: {type(user_id)})")
        print(f"Doctor ID: {doctor_id} (type: {type(doctor_id)})")
        print(f"Symptom ID: {symptom_id} (type: {type(symptom_id)})")
        print(f"Date/Time: {date_time} (type: {type(date_time)})")
        
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if IDs exist
        print("\n--- Checking if IDs exist ---")
        cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
        user_result = cursor.fetchone()
        if not user_result:
            print(f"✗ User ID {user_id} does not exist!")
            conn.close()
            return False
        print(f"✓ User ID {user_id} exists: {user_result}")
        
        cursor.execute("SELECT doctor_id FROM doctors WHERE doctor_id = %s", (doctor_id,))
        doctor_result = cursor.fetchone()
        if not doctor_result:
            print(f"✗ Doctor ID {doctor_id} does not exist!")
            conn.close()
            return False
        print(f"✓ Doctor ID {doctor_id} exists: {doctor_result}")
        
        cursor.execute("SELECT symptom_id FROM symptoms WHERE symptom_id = %s", (symptom_id,))
        symptom_result = cursor.fetchone()
        if not symptom_result:
            print(f"✗ Symptom ID {symptom_id} does not exist!")
            conn.close()
            return False
        print(f"✓ Symptom ID {symptom_id} exists: {symptom_result}")
        
        # Verify the appointment doesn't already exist
        print("\n--- Checking for duplicates ---")
        cursor.execute("""
            SELECT COUNT(*) as appointment_count FROM appointments 
            WHERE user_id = %s AND doctor_id = %s AND date_time = %s
        """, (user_id, doctor_id, date_time))
        
        result = cursor.fetchone()
        print(f"Duplicate check result: {result}")
        
        # Handle both dict and tuple results
        if isinstance(result, dict):
            existing = result.get('appointment_count', 0) or result.get('COUNT(*)', 0)
        else:
            existing = result[0] if result else 0
        
        print(f"Existing count: {existing}")
        
        if existing > 0:
            print(f"⚠ Warning: This exact appointment already exists!")
            conn.close()
            return False
        print("✓ No duplicate found")
        
        # Insert the appointment
        print("\n--- Inserting appointment ---")
        insert_query = """
            INSERT INTO appointments (user_id, doctor_id, symptom_id, date_time)
            VALUES (%s, %s, %s, %s)
        """
        print(f"Query: {insert_query}")
        print(f"Values: ({user_id}, {doctor_id}, {symptom_id}, {date_time})")
        
        cursor.execute(insert_query, (user_id, doctor_id, symptom_id, date_time))
        
        # Get the inserted row ID
        appointment_id = cursor.lastrowid
        print(f"✓ Inserted appointment with ID: {appointment_id}")
        
        if not appointment_id:
            print("⚠ Warning: lastrowid is 0 or None")
        
        # Commit the transaction
        print("\n--- Committing transaction ---")
        conn.commit()
        print(f"✓ Transaction committed successfully")
        
        # Verify the insert
        print("\n--- Verifying insert ---")
        if appointment_id:
            cursor.execute("SELECT * FROM appointments WHERE appointment_id = %s", (appointment_id,))
            inserted = cursor.fetchone()
            print(f"Verification result: {inserted}")
        else:
            # If lastrowid failed, check by other criteria
            cursor.execute("""
                SELECT * FROM appointments 
                WHERE user_id = %s AND doctor_id = %s AND symptom_id = %s AND date_time = %s
            """, (user_id, doctor_id, symptom_id, date_time))
            inserted = cursor.fetchone()
            print(f"Verification by criteria result: {inserted}")
        
        conn.close()
        
        if inserted:
            print(f"✓ Verification successful!")
            return True
        else:
            print("✗ Verification failed: Row not found after commit!")
            return False
        
    except Exception as e:
        print(f"\n✗ ERROR occurred:")
        print(f"  Error type: {type(e).__name__}")
        print(f"  Error message: {str(e)}")
        print(f"  Error args: {e.args}")
        print("\nFull traceback:")
        traceback.print_exc()
        
        if conn:
            try:
                conn.rollback()
                print("\n✓ Transaction rolled back")
                conn.close()
            except Exception as close_error:
                print(f"Error closing connection: {close_error}")
        return False

def get_user_appointments(user_id):
    """Fetch all appointments for a user"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.appointment_id, a.date_time, d.name as doctor_name, 
                   d.specialization, h.name as hospital_name, s.severity_level
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.doctor_id
            LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
            JOIN symptoms s ON a.symptom_id = s.symptom_id
            WHERE a.user_id = %s
            ORDER BY a.date_time DESC
        """, (user_id,))
        appointments = cursor.fetchall()
        conn.close()
        print(f"✓ Fetched {len(appointments)} appointments for user {user_id}")
        return appointments
    except Exception as e:
        print(f"✗ Error fetching appointments: {e}")
        traceback.print_exc()
        return []

def get_doctor_by_id(doctor_id):
    """Fetch a specific doctor's details"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.doctor_id, d.name, d.specialization, h.name as hospital_name, 
                   h.city, d.contact, d.email
            FROM doctors d
            LEFT JOIN hospitals h ON d.hospital_id = h.hospital_id
            WHERE d.doctor_id = %s
        """, (doctor_id,))
        doctor = cursor.fetchone()
        conn.close()
        return doctor
    except Exception as e:
        print(f"✗ Error fetching doctor: {e}")
        traceback.print_exc()
        return None