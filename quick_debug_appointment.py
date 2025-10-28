"""
Quick Debug Script - Run this to find the exact error
"""
from database import get_connection
import traceback

def test_direct_insert():
    """Test inserting appointment directly"""
    print("="*60)
    print("DIRECT APPOINTMENT INSERT TEST")
    print("="*60)
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Test data
        user_id = 1
        doctor_id = 4
        symptom_id = 1
        date_time = "2025-10-28 10:00:00"
        
        print(f"\nAttempting to insert:")
        print(f"  User ID: {user_id}")
        print(f"  Doctor ID: {doctor_id}")
        print(f"  Symptom ID: {symptom_id}")
        print(f"  Date/Time: {date_time}")
        
        # Check if these IDs exist
        print("\n--- Verifying IDs exist ---")
        
        cursor.execute("SELECT user_id, username FROM users WHERE user_id = %s", (user_id,))
        user = cursor.fetchone()
        if user:
            print(f"✓ User exists: {user}")
        else:
            print(f"✗ User ID {user_id} NOT FOUND!")
            conn.close()
            return
        
        cursor.execute("SELECT doctor_id, name FROM doctors WHERE doctor_id = %s", (doctor_id,))
        doctor = cursor.fetchone()
        if doctor:
            print(f"✓ Doctor exists: {doctor}")
        else:
            print(f"✗ Doctor ID {doctor_id} NOT FOUND!")
            conn.close()
            return
        
        cursor.execute("SELECT symptom_id, severity_level FROM symptoms WHERE symptom_id = %s", (symptom_id,))
        symptom = cursor.fetchone()
        if symptom:
            print(f"✓ Symptom exists: {symptom}")
        else:
            print(f"✗ Symptom ID {symptom_id} NOT FOUND!")
            conn.close()
            return
        
        # Check for duplicate
        print("\n--- Checking for duplicates ---")
        cursor.execute("""
            SELECT COUNT(*) as count FROM appointments 
            WHERE user_id = %s AND doctor_id = %s AND date_time = %s
        """, (user_id, doctor_id, date_time))
        
        result = cursor.fetchone()
        # Handle both dict and tuple results
        existing = result['count'] if isinstance(result, dict) else result[0]
        if existing > 0:
            print(f"⚠ Duplicate found! This exact appointment already exists.")
            
            cursor.execute("""
                SELECT * FROM appointments 
                WHERE user_id = %s AND doctor_id = %s AND date_time = %s
            """, (user_id, doctor_id, date_time))
            print(f"Existing appointment: {cursor.fetchone()}")
            conn.close()
            return
        else:
            print("✓ No duplicate found")
        
        # Try to insert
        print("\n--- Attempting INSERT ---")
        cursor.execute("""
            INSERT INTO appointments (user_id, doctor_id, symptom_id, date_time)
            VALUES (%s, %s, %s, %s)
        """, (user_id, doctor_id, symptom_id, date_time))
        
        appointment_id = cursor.lastrowid
        print(f"✓ INSERT successful! Appointment ID: {appointment_id}")
        
        # Commit
        print("\n--- Committing transaction ---")
        conn.commit()
        print("✓ COMMIT successful!")
        
        # Verify
        print("\n--- Verifying insert ---")
        cursor.execute("SELECT * FROM appointments WHERE appointment_id = %s", (appointment_id,))
        result = cursor.fetchone()
        
        if result:
            print(f"✓ Verification successful!")
            print(f"  Inserted row: {result}")
        else:
            print("✗ Verification FAILED! Row not found after commit.")
        
        conn.close()
        print("\n" + "="*60)
        print("TEST COMPLETED SUCCESSFULLY!")
        print("="*60)
        
    except Exception as e:
        print(f"\n✗ ERROR OCCURRED:")
        print(f"  Error Type: {type(e).__name__}")
        print(f"  Error Message: {str(e)}")
        print("\nFull Traceback:")
        traceback.print_exc()
        
        if 'conn' in locals():
            try:
                conn.rollback()
                print("\n✓ Transaction rolled back")
                conn.close()
            except:
                pass

def check_appointments_table_structure():
    """Check the actual structure of appointments table"""
    print("\n" + "="*60)
    print("APPOINTMENTS TABLE STRUCTURE")
    print("="*60)
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DESCRIBE appointments")
        columns = cursor.fetchall()
        
        print("\nColumns:")
        for col in columns:
            print(f"  {col[0]:20s} {col[1]:20s} NULL:{col[2]:5s} KEY:{col[3]:5s} DEFAULT:{col[4]}")
        
        # Check for AUTO_INCREMENT
        cursor.execute("SHOW CREATE TABLE appointments")
        create_stmt = cursor.fetchone()[1]
        
        if "AUTO_INCREMENT" in create_stmt:
            print("\n✓ appointment_id has AUTO_INCREMENT")
        else:
            print("\n✗ appointment_id MISSING AUTO_INCREMENT!")
            print("  This might cause insertion issues!")
        
        conn.close()
        
    except Exception as e:
        print(f"✗ Error: {e}")
        traceback.print_exc()

def show_all_appointments():
    """Show all existing appointments"""
    print("\n" + "="*60)
    print("ALL EXISTING APPOINTMENTS")
    print("="*60)
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM appointments")
        count = cursor.fetchone()[0]
        print(f"\nTotal appointments: {count}")
        
        if count > 0:
            cursor.execute("SELECT * FROM appointments")
            appointments = cursor.fetchall()
            
            print("\nAppointments:")
            for apt in appointments:
                print(f"  {apt}")
        
        conn.close()
        
    except Exception as e:
        print(f"✗ Error: {e}")

if __name__ == "__main__":
    print("\n🔍 QUICK APPOINTMENT DEBUG TOOL\n")
    
    # Check table structure
    check_appointments_table_structure()
    
    # Show existing appointments
    show_all_appointments()
    
    # Test direct insert
    test_direct_insert()
    
    print("\n" + "="*60)
    print("DIAGNOSIS COMPLETE")
    print("="*60)
    print("\nIf you see any ✗ errors above, that's your problem!")
    print("Common issues:")
    print("  1. Missing AUTO_INCREMENT on appointment_id")
    print("  2. Foreign key constraint failure")
    print("  3. Duplicate appointment already exists")
    print("  4. Invalid user/doctor/symptom ID")