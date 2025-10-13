from models.appointment_model import get_hospitals, create_appointment, get_user_appointments

def fetch_hospitals():
    hospitals = get_hospitals()
    print("Fetched hospitals:", hospitals)  # Debug print
    return hospitals

def book_appointment(user_id, hospital_id, symptom_id, date_time):
    create_appointment(user_id, hospital_id, symptom_id, date_time)

def fetch_user_appointments(user_id):
    return get_user_appointments(user_id)
