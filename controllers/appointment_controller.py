# # # from models.appointment_model import get_hospitals, create_appointment, get_user_appointments

# # # def fetch_hospitals():
# # #     hospitals = get_hospitals()
# # #     print("Fetched hospitals:", hospitals)  # Debug print
# # #     return hospitals

# # # def book_appointment(user_id, hospital_id, symptom_id, date_time):
# # #     create_appointment(user_id, hospital_id, symptom_id, date_time)

# # # def fetch_user_appointments(user_id):
# # #     return get_user_appointments(user_id)


# # from models.appointment_model import get_hospitals, create_appointment, get_user_appointments

# # def fetch_hospitals():
# #     hospitals = get_hospitals()
# #     print("Fetched hospitals:", hospitals)  # Debug print
    
# #     # Convert tuples to dictionaries for easier access
# #     if hospitals and not isinstance(hospitals[0], dict):
# #         hospital_list = []
# #         for h in hospitals:
# #             hospital_dict = {
# #                 'hospital_id': h[0],
# #                 'name': h[1],
# #                 'city': h[2],
# #                 'contact': h[3] if len(h) > 3 else None,
# #                 'booking_link': h[4] if len(h) > 4 else None,
# #                 'created_at': h[5] if len(h) > 5 else None
# #             }
# #             hospital_list.append(hospital_dict)
# #         return hospital_list
    
# #     return hospitals

# # def book_appointment(user_id, hospital_id, symptom_id, date_time):
# #     create_appointment(user_id, hospital_id, symptom_id, date_time)

# # def fetch_user_appointments(user_id):
# #     return get_user_appointments(user_id)


# from models.appointment_model import get_hospitals, create_appointment, get_user_appointments

# def fetch_hospitals():
#     print("\n=== Fetching Hospitals ===")
#     hospitals = get_hospitals()
#     print(f"Raw hospitals data: {hospitals}")
    
#     # Convert tuples to dictionaries for easier access
#     if hospitals and not isinstance(hospitals[0], dict):
#         hospital_list = []
#         for h in hospitals:
#             hospital_dict = {
#                 'hospital_id': h[0],
#                 'name': h[1],
#                 'city': h[2],
#                 'contact': h[3] if len(h) > 3 else None,
#                 'booking_link': h[4] if len(h) > 4 else None,
#                 'created_at': h[5] if len(h) > 5 else None
#             }
#             hospital_list.append(hospital_dict)
#             print(f"  - {hospital_dict['name']} (ID: {hospital_dict['hospital_id']})")
#         return hospital_list
    
#     return hospitals

# def book_appointment(user_id, hospital_id, symptom_id, date_time):
#     print(f"\n=== Booking Appointment (Controller) ===")
#     print(f"Input parameters:")
#     print(f"  User ID: {user_id} (type: {type(user_id)})")
#     print(f"  Hospital ID: {hospital_id} (type: {type(hospital_id)})")
#     print(f"  Symptom ID: {symptom_id} (type: {type(symptom_id)})")
#     print(f"  Date/Time: {date_time} (type: {type(date_time)})")
    
#     result = create_appointment(user_id, hospital_id, symptom_id, date_time)
    
#     if result:
#         print("✓ Appointment booked successfully!")
#     else:
#         print("✗ Failed to book appointment")
    
#     return result

# def fetch_user_appointments(user_id):
#     print(f"\n=== Fetching User Appointments ===")
#     print(f"User ID: {user_id}")
#     return get_user_appointments(user_id)



# from models.appointment_model import (
#     get_doctors, 
#     get_doctors_by_specialization,
#     get_all_specializations,
#     create_appointment, 
#     get_user_appointments,
#     get_doctor_by_id
# )

# def fetch_doctors(specialization=None):
#     """Fetch all doctors or filter by specialization"""
#     print("\n=== Fetching Doctors ===")
    
#     if specialization and specialization != "All Specializations":
#         doctors = get_doctors_by_specialization(specialization)
#     else:
#         doctors = get_doctors()
    
#     print(f"Raw doctors data: {doctors}")
    
#     # Convert tuples to dictionaries for easier access
#     if doctors and not isinstance(doctors[0], dict):
#         doctor_list = []
#         for d in doctors:
#             doctor_dict = {
#                 'doctor_id': d[0],
#                 'name': d[1],
#                 'specialization': d[2],
#                 'hospital_name': d[3] if len(d) > 3 else 'N/A',
#                 'city': d[4] if len(d) > 4 else 'N/A',
#                 'contact': d[5] if len(d) > 5 else 'N/A',
#                 'email': d[6] if len(d) > 6 else 'N/A'
#             }
#             doctor_list.append(doctor_dict)
#             print(f"  - Dr. {doctor_dict['name']} ({doctor_dict['specialization']}) - {doctor_dict['hospital_name']}")
#         return doctor_list
    
#     return doctors

# def fetch_specializations():
#     """Fetch all unique specializations"""
#     return get_all_specializations()

# def book_appointment(user_id, doctor_id, symptom_id, date_time):
#     """Book an appointment with a doctor"""
#     print(f"\n=== Booking Appointment (Controller) ===")
#     print(f"Input parameters:")
#     print(f"  User ID: {user_id} (type: {type(user_id)})")
#     print(f"  Doctor ID: {doctor_id} (type: {type(doctor_id)})")
#     print(f"  Symptom ID: {symptom_id} (type: {type(symptom_id)})")
#     print(f"  Date/Time: {date_time} (type: {type(date_time)})")
    
#     result = create_appointment(user_id, doctor_id, symptom_id, date_time)
    
#     if result:
#         print("✓ Appointment booked successfully!")
#     else:
#         print("✗ Failed to book appointment")
    
#     return result

# def fetch_user_appointments(user_id):
#     """Fetch all appointments for a user"""
#     print(f"\n=== Fetching User Appointments ===")
#     print(f"User ID: {user_id}")
#     return get_user_appointments(user_id)

# def fetch_doctor_details(doctor_id):
#     """Fetch details of a specific doctor"""
#     return get_doctor_by_id(doctor_id)



from models.appointment_model import (
    get_doctors, 
    get_doctors_by_specialization,
    get_all_specializations,
    create_appointment, 
    get_user_appointments,
    get_doctor_by_id
)

def fetch_doctors(specialization=None):
    """Fetch all doctors or filter by specialization"""
    print("\n=== Fetching Doctors ===")
    
    if specialization and specialization != "All Specializations":
        doctors = get_doctors_by_specialization(specialization)
    else:
        doctors = get_doctors()
    
    print(f"Raw doctors data (first item): {doctors[0] if doctors else 'None'}")
    print(f"Type: {type(doctors[0]) if doctors else 'N/A'}")
    
    # Convert to dictionaries for easier access
    if doctors and not isinstance(doctors[0], dict):
        doctor_list = []
        for d in doctors:
            doctor_dict = {
                'doctor_id': d[0],
                'name': d[1],
                'specialization': d[2],
                'hospital_name': d[3] if len(d) > 3 else 'N/A',
                'city': d[4] if len(d) > 4 else 'N/A',
                'contact': d[5] if len(d) > 5 else 'N/A',
                'email': d[6] if len(d) > 6 else 'N/A'
            }
            doctor_list.append(doctor_dict)
            print(f"  - Dr. {doctor_dict['name']} ({doctor_dict['specialization']}) - {doctor_dict['hospital_name']}")
        return doctor_list
    elif doctors and isinstance(doctors[0], dict):
        # Already dictionaries
        for d in doctors:
            print(f"  - Dr. {d.get('name')} ({d.get('specialization')}) - {d.get('hospital_name')}")
        return doctors
    
    return doctors

def fetch_specializations():
    """Fetch all unique specializations"""
    return get_all_specializations()

def book_appointment(user_id, doctor_id, symptom_id, date_time):
    """Book an appointment with a doctor"""
    print(f"\n=== Booking Appointment (Controller) ===")
    print(f"Input parameters:")
    print(f"  User ID: {user_id} (type: {type(user_id)})")
    print(f"  Doctor ID: {doctor_id} (type: {type(doctor_id)})")
    print(f"  Symptom ID: {symptom_id} (type: {type(symptom_id)})")
    print(f"  Date/Time: {date_time} (type: {type(date_time)})")
    
    result = create_appointment(user_id, doctor_id, symptom_id, date_time)
    
    if result:
        print("✓ Appointment booked successfully!")
    else:
        print("✗ Failed to book appointment")
    
    return result

def fetch_user_appointments(user_id):
    """Fetch all appointments for a user"""
    print(f"\n=== Fetching User Appointments ===")
    print(f"User ID: {user_id}")
    return get_user_appointments(user_id)

def fetch_doctor_details(doctor_id):
    """Fetch details of a specific doctor"""
    return get_doctor_by_id(doctor_id)