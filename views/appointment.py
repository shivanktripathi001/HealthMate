# import streamlit as st
# from controllers.appointment_controller import fetch_hospitals, book_appointment
# from controllers.symptom_controller import get_symptom_id

# def render():
#     st.title("Book Appointment")

#     if not st.session_state.get("logged_in"):
#         st.warning("Please log in to book an appointment.")
#         st.stop()

#     hospitals = fetch_hospitals()
#     hospital_names = [f"{h[1]} ({h[2]})" for h in hospitals]
#     selected_index = st.selectbox("Choose a hospital", range(len(hospital_names)), format_func=lambda i: hospital_names[i])
#     selected_hospital_id = hospitals[selected_index][0]

#     date = st.date_input("Select a date")
#     time = st.time_input("Select a time")

#     if st.button("Book Appointment"):
#         symptom_name = st.session_state.get("selected_symptom", None)
#         if not symptom_name:
#             st.error("Please check a symptom first.")
#         else:
#             symptom_id = get_symptom_id(symptom_name)
#             dt = f"{date} {time}"
#             book_appointment(st.session_state["user_id"], selected_hospital_id, symptom_id, dt)
#             st.success("Appointment booked successfully!")







# import streamlit as st
# from controllers.appointment_controller import fetch_hospitals, book_appointment
# from controllers.symptom_controller import get_symptom_id

# def render():
#     st.title("Book Appointment")

#     if not st.session_state.get("logged_in"):
#         st.warning("Please log in to book an appointment.")
#         st.stop()

#     hospitals = fetch_hospitals()

#     if not hospitals:
#         st.error("No hospitals available. Please check your data source.")
#         return

#     hospital_names = [f"{h[1]} ({h[2]})" for h in hospitals]
#     selected_index = st.selectbox(
#         "Choose a hospital",
#         options=range(len(hospital_names)),
#         format_func=lambda i: hospital_names[i]
#     )

#     if selected_index is None:
#         st.error("Please select a hospital.")
#         return

#     selected_hospital_id = hospitals[selected_index][0]

#     date = st.date_input("Select a date")
#     time = st.time_input("Select a time")

#     if st.button("Book Appointment"):
#         symptom_name = st.session_state.get("selected_symptom", None)
#         if not symptom_name:
#             st.error("Please check a symptom first.")
#         else:
#             symptom_id = get_symptom_id(symptom_name)
#             if symptom_id is None:
#                 st.error("Could not find symptom ID.")
#                 return
#             dt = f"{date} {time}"
#             book_appointment(st.session_state["user_id"], selected_hospital_id, symptom_id, dt)
#             st.success("Appointment booked successfully!")


# import streamlit as st
# from controllers.appointment_controller import fetch_hospitals, book_appointment
# from controllers.symptom_controller import get_symptom_id

# def render():
#     st.title("Book Appointment")

#     if not st.session_state.get("logged_in"):
#         st.warning("Please log in to book an appointment.")
#         st.stop()

#     hospitals = fetch_hospitals()

#     if not hospitals:
#         st.error("No hospitals available. Please check your database or insert sample data.")
#         return

#     hospital_names = [f"{h[1]} ({h[2]})" for h in hospitals]
#     selected_index = st.selectbox(
#         "Choose a hospital",
#         options=range(len(hospital_names)),
#         format_func=lambda i: hospital_names[i]
#     )

#     selected_hospital_id = hospitals[selected_index][0]

#     date = st.date_input("Select a date")
#     time = st.time_input("Select a time")

#     if st.button("Book Appointment"):
#         symptom_name = st.session_state.get("selected_symptom", None)
#         if not symptom_name:
#             st.error("Please check a symptom first.")
#         else:
#             symptom_id = get_symptom_id(symptom_name)
#             if symptom_id is None:
#                 st.error("Could not find symptom ID.")
#                 return
#             dt = f"{date} {time}"
#             book_appointment(st.session_state["user_id"], selected_hospital_id, symptom_id, dt)
#             st.success("Appointment booked successfully!")



import streamlit as st
from controllers.appointment_controller import fetch_hospitals, book_appointment
from controllers.symptom_controller import get_symptom_id
 
def render():
    st.title("Book Appointment")
    if not st.session_state.get("logged_in"):
        st.warning("Please log in to book an appointment.")
        st.stop()
        
    hospitals = fetch_hospitals()
    
    if not hospitals:
        st.error("No hospitals available. Please check your database or insert sample data.")
        return
        
    # Modified line to access dictionary keys instead of list indices
    hospital_names = [f"{h['name']} ({h['location']})" for h in hospitals]
    
    selected_index = st.selectbox(
        "Choose a hospital",
        options=range(len(hospital_names)),
        format_func=lambda i: hospital_names[i]
    )
    
    # Assuming 'hospital_id' is the correct key
    selected_hospital_id = hospitals[selected_index]['hospital_id']
    
    date = st.date_input("Select a date")
    time = st.time_input("Select a time")
    
    if st.button("Book Appointment"):
        symptom_name = st.session_state.get("selected_symptom", None)
        if not symptom_name:
            st.error("Please check a symptom first.")
        else:
            symptom_id = get_symptom_id(symptom_name)
            if symptom_id is None:
                st.error("Could not find symptom ID.")
                return
            dt = f"{date} {time}"
            book_appointment(st.session_state["user_id"], selected_hospital_id, symptom_id, dt)
            st.success("Appointment booked successfully!")
 





