# from models.appointment_model import get_hospitals, create_appointment, get_user_appointments

# def fetch_hospitals():
#     hospitals = get_hospitals()
#     print("Fetched hospitals:", hospitals)  # Debug print
#     return hospitals

# def book_appointment(user_id, hospital_id, symptom_id, date_time):
#     create_appointment(user_id, hospital_id, symptom_id, date_time)

# def fetch_user_appointments(user_id):
#     return get_user_appointments(user_id)


from models.appointment_model import get_hospitals, create_appointment, get_user_appointments

def fetch_hospitals():
    hospitals = get_hospitals()
    print("Fetched hospitals:", hospitals)  # Debug print
    
    # Convert tuples to dictionaries for easier access
    if hospitals and not isinstance(hospitals[0], dict):
        hospital_list = []
        for h in hospitals:
            hospital_dict = {
                'hospital_id': h[0],
                'name': h[1],
                'city': h[2],
                'contact': h[3] if len(h) > 3 else None,
                'booking_link': h[4] if len(h) > 4 else None,
                'created_at': h[5] if len(h) > 5 else None
            }
            hospital_list.append(hospital_dict)
        return hospital_list
    
    return hospitals

def book_appointment(user_id, hospital_id, symptom_id, date_time):
    create_appointment(user_id, hospital_id, symptom_id, date_time)

def fetch_user_appointments(user_id):
    return get_user_appointments(user_id)
