# import streamlit as st
# from models.doctor_model import get_doctor_by_username, get_all_appointments_for_hospital, update_appointment_status

# def handle_doctor_login(username, password):
#     """Handle doctor login"""
#     doctor = get_doctor_by_username(username)
#     if doctor and doctor["password"] == password:
#         st.session_state["doctor_logged_in"] = True
#         st.session_state["doctor_id"] = doctor["doctor_id"]
#         st.session_state["doctor_name"] = doctor["name"]
#         st.session_state["doctor_hospital_id"] = doctor["hospital_id"]
#         st.session_state["doctor_specialization"] = doctor["specialization"]
#         return True
#     return False

# def fetch_hospital_appointments(hospital_id):
#     """Fetch all appointments for doctor's hospital"""
#     return get_all_appointments_for_hospital(hospital_id)

# def change_appointment_status(appointment_id, status):
#     """Change appointment status"""
#     return update_appointment_status(appointment_id, status)


import streamlit as st
from models.doctor_model import (
    get_doctor_by_username, 
    get_all_appointments_for_doctor,
    get_all_appointments_for_hospital, 
    update_appointment_status
)

def handle_doctor_login(username, password):
    """Handle doctor login"""
    doctor = get_doctor_by_username(username)
    if doctor and doctor["password"] == password:
        st.session_state["doctor_logged_in"] = True
        st.session_state["doctor_id"] = doctor["doctor_id"]
        st.session_state["doctor_name"] = doctor["name"]
        st.session_state["doctor_hospital_id"] = doctor["hospital_id"]
        st.session_state["doctor_specialization"] = doctor["specialization"]
        return True
    return False

def fetch_doctor_appointments(doctor_id):
    """Fetch all appointments for a specific doctor"""
    return get_all_appointments_for_doctor(doctor_id)

def fetch_hospital_appointments(hospital_id):
    """Fetch all appointments for doctor's hospital"""
    return get_all_appointments_for_hospital(hospital_id)

def change_appointment_status(appointment_id, status):
    """Change appointment status"""
    return update_appointment_status(appointment_id, status)