

# import streamlit as st
# from controllers.appointment_controller import (
#     fetch_doctors, 
#     fetch_specializations,
#     book_appointment
# )
# from controllers.symptom_controller import get_symptom_id
# from datetime import datetime, timedelta
 
# def render():
#     st.title("🏥 Book Appointment with Doctor")
    
#     # Check if user is logged in
#     if not st.session_state.get("logged_in"):
#         st.warning("⚠️ Please log in to book an appointment.")
#         st.stop()
    
#     # Debug: Show session state
#     with st.expander("🔍 Debug: Session State"):
#         st.write("Logged in:", st.session_state.get("logged_in"))
#         st.write("User ID:", st.session_state.get("user_id"))
#         st.write("Selected Symptom:", st.session_state.get("selected_symptom"))
    
#     st.markdown("---")
    
#     # Specialization filter
#     st.subheader("🔍 Filter by Specialization")
#     specializations = fetch_specializations()
    
#     if specializations:
#         specialization_options = ["All Specializations"] + specializations
#         selected_specialization = st.selectbox(
#             "Select Specialization",
#             options=specialization_options,
#             help="Filter doctors by their specialization"
#         )
#     else:
#         selected_specialization = None
#         st.info("No specializations available")
    
#     # Fetch doctors
#     doctors = fetch_doctors(selected_specialization if selected_specialization != "All Specializations" else None)
    
#     if not doctors:
#         st.error("❌ No doctors available. Please add doctors to the database.")
        
#         # Show SQL to add sample doctors
#         with st.expander("💡 Add Sample Doctors"):
#             st.code("""
# INSERT INTO doctors (username, password, name, specialization, hospital_id, email, contact) 
# VALUES 
# ('dr.sharma', 'doctor123', 'Dr. Amit Sharma', 'Cardiologist', 1, 'amit.sharma@hospital.com', '+91-9876543210'),
# ('dr.patel', 'doctor123', 'Dr. Priya Patel', 'Neurologist', 2, 'priya.patel@hospital.com', '+91-9876543211'),
# ('dr.kumar', 'doctor123', 'Dr. Rajesh Kumar', 'Orthopedic', 3, 'rajesh.kumar@hospital.com', '+91-9876543212');
#             """, language="sql")
#         return
    
#     # Display doctor selection
#     st.subheader("👨‍⚕️ Select Doctor")
    
#     # Create a more detailed display for doctors
#     doctor_options = []
#     for d in doctors:
#         if isinstance(d, dict):
#             display_text = f"Dr. {d['name']} - {d['specialization']} ({d['hospital_name']}, {d['city']})"
#             doctor_options.append(display_text)
#         else:
#             display_text = f"Dr. {d[1]} - {d[2]} ({d[3]}, {d[4]})"
#             doctor_options.append(display_text)
    
#     selected_doctor_index = st.selectbox(
#         "Choose a doctor",
#         options=range(len(doctor_options)),
#         format_func=lambda i: doctor_options[i]
#     )
    
#     # Get selected doctor details
#     selected_doctor = doctors[selected_doctor_index]
    
#     if isinstance(selected_doctor, dict):
#         doctor_id = selected_doctor['doctor_id']
#         doctor_name = selected_doctor['name']
#         doctor_spec = selected_doctor['specialization']
#         doctor_hospital = selected_doctor['hospital_name']
#         doctor_city = selected_doctor['city']
#         doctor_contact = selected_doctor['contact']
#     else:
#         doctor_id = selected_doctor[0]
#         doctor_name = selected_doctor[1]
#         doctor_spec = selected_doctor[2]
#         doctor_hospital = selected_doctor[3]
#         doctor_city = selected_doctor[4]
#         doctor_contact = selected_doctor[5]
    
#     # Show doctor details
#     st.info(f"""
#     **👨‍⚕️ Doctor Details:**
#     - **Name:** Dr. {doctor_name}
#     - **Specialization:** {doctor_spec}
#     - **Hospital:** {doctor_hospital}
#     - **Location:** {doctor_city}
#     - **Contact:** {doctor_contact}
#     """)
    
#     st.markdown("---")
    
#     # Date and time selection
#     st.subheader("📅 Select Appointment Date & Time")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         min_date = datetime.now().date()
#         max_date = min_date + timedelta(days=30)  # Allow booking up to 30 days in advance
#         date = st.date_input(
#             "Appointment Date", 
#             min_value=min_date,
#             max_value=max_date,
#             help="Select a date within the next 30 days"
#         )
    
#     with col2:
#         time = st.time_input(
#             "Appointment Time",
#             value=datetime.strptime("10:00", "%H:%M").time(),
#             help="Select appointment time"
#         )
    
#     # Show appointment summary
#     st.markdown("---")
#     st.subheader("📋 Appointment Summary")
    
#     symptom_name = st.session_state.get('selected_symptom', 'Not selected')
    
#     summary_col1, summary_col2 = st.columns(2)
    
#     with summary_col1:
#         st.write("**Doctor:**", f"Dr. {doctor_name}")
#         st.write("**Specialization:**", doctor_spec)
#         st.write("**Hospital:**", doctor_hospital)
    
#     with summary_col2:
#         st.write("**Date:**", date.strftime("%B %d, %Y"))
#         st.write("**Time:**", time.strftime("%I:%M %p"))
#         st.write("**Symptom:**", symptom_name)
    
#     # Book appointment button
#     st.markdown("---")
    
#     if st.button("📅 Confirm Booking", type="primary", use_container_width=True):
#         # Validate symptom
#         if not symptom_name or symptom_name == 'Not selected':
#             st.error("❌ Please check a symptom first using the Symptom Checker.")
#             st.info("💡 Go to 'Symptom Checker' page and select your symptoms before booking.")
#             return
        
#         # Get symptom ID
#         symptom_id = get_symptom_id(symptom_name)
        
#         if symptom_id is None:
#             st.error(f"❌ Could not find symptom ID for '{symptom_name}'.")
#             st.info("💡 Try checking the symptom again in the Symptom Checker.")
#             return
        
#         # Format datetime
#         dt = f"{date} {time}"
        
#         # Debug info
#         with st.expander("🔍 Debug: Booking Parameters"):
#             st.write(f"User ID: {st.session_state['user_id']}")
#             st.write(f"Doctor ID: {doctor_id}")
#             st.write(f"Symptom ID: {symptom_id}")
#             st.write(f"Date/Time: {dt}")
        
#         # Book the appointment
#         try:
#             result = book_appointment(
#                 st.session_state["user_id"], 
#                 doctor_id, 
#                 symptom_id, 
#                 dt
#             )
            
#             if result:
#                 st.success("✅ Appointment booked successfully!")
#                 st.balloons()
                
#                 # Show confirmation card
#                 st.markdown("---")
#                 st.markdown("### 🎉 Booking Confirmed!")
                
#                 st.success(f"""
#                 **Your appointment has been scheduled:**
                
#                 📅 **Date:** {date.strftime("%B %d, %Y")}  
#                 🕐 **Time:** {time.strftime("%I:%M %p")}  
#                 👨‍⚕️ **Doctor:** Dr. {doctor_name}  
#                 🏥 **Hospital:** {doctor_hospital}, {doctor_city}  
#                 📞 **Contact:** {doctor_contact}  
#                 🩺 **Symptom:** {symptom_name}
                
#                 Please arrive 15 minutes before your scheduled time.
#                 """)
                
#                 # Clear the selected symptom after booking
#                 if st.button("Book Another Appointment"):
#                     st.session_state['selected_symptom'] = None
#                     st.rerun()
#             else:
#                 st.error("❌ Failed to book appointment. This time slot might already be booked.")
#                 st.info("Please try selecting a different date or time.")
                
#         except Exception as e:
#             st.error(f"❌ Error booking appointment: {str(e)}")
#             st.exception(e)



# import streamlit as st
# from controllers.appointment_controller import (
#     fetch_doctors, 
#     fetch_specializations,
#     book_appointment
# )
# from controllers.symptom_controller import get_symptom_id
# from datetime import datetime, timedelta
 
# def render():
#     st.title("🏥 Book Appointment with Doctor")
    
#     # Check if user is logged in
#     if not st.session_state.get("logged_in"):
#         st.warning("⚠️ Please log in to book an appointment.")
#         st.stop()
    
#     # Debug: Show session state
#     with st.expander("🔍 Debug: Session State"):
#         st.write("Logged in:", st.session_state.get("logged_in"))
#         st.write("User ID:", st.session_state.get("user_id"))
#         st.write("Selected Symptom:", st.session_state.get("selected_symptom"))
    
#     st.markdown("---")
    
#     # Specialization filter
#     st.subheader("🔍 Filter by Specialization")
#     specializations = fetch_specializations()
    
#     if specializations:
#         specialization_options = ["All Specializations"] + specializations
#         selected_specialization = st.selectbox(
#             "Select Specialization",
#             options=specialization_options,
#             help="Filter doctors by their specialization"
#         )
#     else:
#         selected_specialization = None
#         st.info("No specializations available")
    
#     # Fetch doctors
#     doctors = fetch_doctors(selected_specialization if selected_specialization != "All Specializations" else None)
    
#     if not doctors:
#         st.error("❌ No doctors available. Please add doctors to the database.")
        
#         # Show SQL to add sample doctors
#         with st.expander("💡 Add Sample Doctors"):
#             st.code("""
# INSERT INTO doctors (username, password, name, specialization, hospital_id, email, contact) 
# VALUES 
# ('dr.sharma', 'doctor123', 'Dr. Amit Sharma', 'Cardiologist', 1, 'amit.sharma@hospital.com', '+91-9876543210'),
# ('dr.patel', 'doctor123', 'Dr. Priya Patel', 'Neurologist', 2, 'priya.patel@hospital.com', '+91-9876543211'),
# ('dr.kumar', 'doctor123', 'Dr. Rajesh Kumar', 'Orthopedic', 3, 'rajesh.kumar@hospital.com', '+91-9876543212');
#             """, language="sql")
#         return
    
#     # Display doctor selection
#     st.subheader("👨‍⚕️ Select Doctor")
    
#     # Create a more detailed display for doctors
#     doctor_options = []
#     for d in doctors:
#         if isinstance(d, dict):
#             display_text = f"Dr. {d['name']} - {d['specialization']} ({d['hospital_name']}, {d['city']})"
#             doctor_options.append(display_text)
#         else:
#             display_text = f"Dr. {d[1]} - {d[2]} ({d[3]}, {d[4]})"
#             doctor_options.append(display_text)
    
#     selected_doctor_index = st.selectbox(
#         "Choose a doctor",
#         options=range(len(doctor_options)),
#         format_func=lambda i: doctor_options[i]
#     )
    
#     # Get selected doctor details
#     selected_doctor = doctors[selected_doctor_index]
    
#     if isinstance(selected_doctor, dict):
#         doctor_id = selected_doctor['doctor_id']
#         doctor_name = selected_doctor['name']
#         doctor_spec = selected_doctor['specialization']
#         doctor_hospital = selected_doctor['hospital_name']
#         doctor_city = selected_doctor['city']
#         doctor_contact = selected_doctor['contact']
#     else:
#         doctor_id = selected_doctor[0]
#         doctor_name = selected_doctor[1]
#         doctor_spec = selected_doctor[2]
#         doctor_hospital = selected_doctor[3]
#         doctor_city = selected_doctor[4]
#         doctor_contact = selected_doctor[5]
    
#     # Show doctor details
#     st.info(f"""
#     **👨‍⚕️ Doctor Details:**
#     - **Name:** Dr. {doctor_name}
#     - **Specialization:** {doctor_spec}
#     - **Hospital:** {doctor_hospital}
#     - **Location:** {doctor_city}
#     - **Contact:** {doctor_contact}
#     """)
    
#     st.markdown("---")
    
#     # Date and time selection
#     st.subheader("📅 Select Appointment Date & Time")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         min_date = datetime.now().date()
#         max_date = min_date + timedelta(days=30)  # Allow booking up to 30 days in advance
#         date = st.date_input(
#             "Appointment Date", 
#             min_value=min_date,
#             max_value=max_date,
#             help="Select a date within the next 30 days"
#         )
    
#     with col2:
#         time = st.time_input(
#             "Appointment Time",
#             value=datetime.strptime("10:00", "%H:%M").time(),
#             help="Select appointment time"
#         )
    
#     # Show appointment summary
#     st.markdown("---")
#     st.subheader("📋 Appointment Summary")
    
#     symptom_name = st.session_state.get('selected_symptom', 'Not selected')
    
#     summary_col1, summary_col2 = st.columns(2)
    
#     with summary_col1:
#         st.write("**Doctor:**", f"Dr. {doctor_name}")
#         st.write("**Specialization:**", doctor_spec)
#         st.write("**Hospital:**", doctor_hospital)
    
#     with summary_col2:
#         st.write("**Date:**", date.strftime("%B %d, %Y"))
#         st.write("**Time:**", time.strftime("%I:%M %p"))
#         st.write("**Symptom:**", symptom_name)
    
#     # Book appointment button
#     st.markdown("---")
    
#     if st.button("📅 Confirm Booking", type="primary", use_container_width=True):
#         # Validate symptom
#         if not symptom_name or symptom_name == 'Not selected':
#             st.error("❌ Please check a symptom first using the Symptom Checker.")
#             st.info("💡 Go to 'Symptom Checker' page and select your symptoms before booking.")
#             return
        
#         # Get symptom ID
#         symptom_id = get_symptom_id(symptom_name)
        
#         if symptom_id is None:
#             st.error(f"❌ Could not find symptom ID for '{symptom_name}'.")
#             st.info("💡 Try checking the symptom again in the Symptom Checker.")
#             return
        
#         # Format datetime
#         dt = f"{date} {time}"
        
#         # Debug info
#         with st.expander("🔍 Debug: Booking Parameters"):
#             st.write(f"User ID: {st.session_state['user_id']}")
#             st.write(f"Doctor ID: {doctor_id}")
#             st.write(f"Symptom ID: {symptom_id}")
#             st.write(f"Date/Time: {dt}")
        
#         # Book the appointment
#         try:
#             result = book_appointment(
#                 st.session_state["user_id"], 
#                 doctor_id, 
#                 symptom_id, 
#                 dt
#             )
            
#             if result:
#                 # Simple success message with checkmark
#                 st.markdown("---")
#                 st.markdown(
#                     """
#                     <div style="text-align: center; padding: 2rem;">
#                         <div style="font-size: 80px; color: #28a745;">✓</div>
#                         <h2 style="color: #28a745; margin-top: 1rem;">Your Appointment Booked Successfully!</h2>
#                     </div>
#                     """, 
#                     unsafe_allow_html=True
#                 )
#                 st.balloons()
#             else:
#                 st.error("❌ Failed to book appointment. This time slot might already be booked.")
#                 st.info("Please try selecting a different date or time.")
                
#         except Exception as e:
#             st.error(f"❌ Error booking appointment: {str(e)}")
#             st.exception(e)


import streamlit as st
from controllers.appointment_controller import (
    fetch_doctors, 
    fetch_specializations,
    book_appointment
)
from controllers.symptom_controller import get_symptom_id
from datetime import datetime, timedelta
 
def render():
    st.title("🏥 Book Appointment with Doctor")
    
    # Check if user is logged in
    if not st.session_state.get("logged_in"):
        st.warning("⚠️ Please log in to book an appointment.")
        st.stop()
    
    # Debug: Show session state
    with st.expander("🔍 Debug: Session State"):
        st.write("Logged in:", st.session_state.get("logged_in"))
        st.write("User ID:", st.session_state.get("user_id"))
        st.write("Selected Symptom:", st.session_state.get("selected_symptom"))
    
    st.markdown("---")
    
    # Specialization filter
    st.subheader("🔍 Filter by Specialization")
    specializations = fetch_specializations()
    
    if specializations:
        specialization_options = ["All Specializations"] + specializations
        selected_specialization = st.selectbox(
            "Select Specialization",
            options=specialization_options,
            help="Filter doctors by their specialization"
        )
    else:
        selected_specialization = None
        st.info("No specializations available")
    
    # Fetch doctors
    doctors = fetch_doctors(selected_specialization if selected_specialization != "All Specializations" else None)
    
    if not doctors:
        st.error("❌ No doctors available. Please add doctors to the database.")
        
        # Show SQL to add sample doctors
        with st.expander("💡 Add Sample Doctors"):
            st.code("""
INSERT INTO doctors (username, password, name, specialization, hospital_id, email, contact) 
VALUES 
('dr.sharma', 'doctor123', 'Dr. Amit Sharma', 'Cardiologist', 1, 'amit.sharma@hospital.com', '+91-9876543210'),
('dr.patel', 'doctor123', 'Dr. Priya Patel', 'Neurologist', 2, 'priya.patel@hospital.com', '+91-9876543211'),
('dr.kumar', 'doctor123', 'Dr. Rajesh Kumar', 'Orthopedic', 3, 'rajesh.kumar@hospital.com', '+91-9876543212');
            """, language="sql")
        return
    
    # Display doctor selection
    st.subheader("👨‍⚕️ Select Doctor")
    
    # Create a more detailed display for doctors
    doctor_options = []
    for d in doctors:
        if isinstance(d, dict):
            display_text = f"Dr. {d['name']} - {d['specialization']} ({d['hospital_name']}, {d['city']})"
            doctor_options.append(display_text)
        else:
            display_text = f"Dr. {d[1]} - {d[2]} ({d[3]}, {d[4]})"
            doctor_options.append(display_text)
    
    selected_doctor_index = st.selectbox(
        "Choose a doctor",
        options=range(len(doctor_options)),
        format_func=lambda i: doctor_options[i]
    )
    
    # Get selected doctor details
    selected_doctor = doctors[selected_doctor_index]
    
    if isinstance(selected_doctor, dict):
        doctor_id = selected_doctor['doctor_id']
        doctor_name = selected_doctor['name']
        doctor_spec = selected_doctor['specialization']
        doctor_hospital = selected_doctor['hospital_name']
        doctor_city = selected_doctor['city']
        doctor_contact = selected_doctor['contact']
    else:
        doctor_id = selected_doctor[0]
        doctor_name = selected_doctor[1]
        doctor_spec = selected_doctor[2]
        doctor_hospital = selected_doctor[3]
        doctor_city = selected_doctor[4]
        doctor_contact = selected_doctor[5]
    
    # Show doctor details
    st.info(f"""
    **👨‍⚕️ Doctor Details:**
    - **Name:** Dr. {doctor_name}
    - **Specialization:** {doctor_spec}
    - **Hospital:** {doctor_hospital}
    - **Location:** {doctor_city}
    - **Contact:** {doctor_contact}
    """)
    
    st.markdown("---")
    
    # Date and time selection
    st.subheader("📅 Select Appointment Date & Time")
    
    col1, col2 = st.columns(2)
    
    with col1:
        min_date = datetime.now().date()
        max_date = min_date + timedelta(days=30)  # Allow booking up to 30 days in advance
        date = st.date_input(
            "Appointment Date", 
            min_value=min_date,
            max_value=max_date,
            help="Select a date within the next 30 days"
        )
    
    with col2:
        time = st.time_input(
            "Appointment Time",
            value=datetime.strptime("10:00", "%H:%M").time(),
            help="Select appointment time"
        )
    
    # Show appointment summary
    st.markdown("---")
    st.subheader("📋 Appointment Summary")
    
    symptom_name = st.session_state.get('selected_symptom', 'Not selected')
    
    summary_col1, summary_col2 = st.columns(2)
    
    with summary_col1:
        st.write("**Doctor:**", f"Dr. {doctor_name}")
        st.write("**Specialization:**", doctor_spec)
        st.write("**Hospital:**", doctor_hospital)
    
    with summary_col2:
        st.write("**Date:**", date.strftime("%B %d, %Y"))
        st.write("**Time:**", time.strftime("%I:%M %p"))
        st.write("**Symptom:**", symptom_name)
    
    # Book appointment button
    st.markdown("---")
    
    if st.button("📅 Confirm Booking", type="primary", use_container_width=True):
        # Validate symptom
        if not symptom_name or symptom_name == 'Not selected':
            st.error("❌ Please check a symptom first using the Symptom Checker.")
            st.info("💡 Go to 'Symptom Checker' page and select your symptoms before booking.")
            return
        
        # Get symptom ID
        symptom_id = get_symptom_id(symptom_name)
        
        if symptom_id is None:
            st.error(f"❌ Could not find symptom ID for '{symptom_name}'.")
            st.info("💡 Try checking the symptom again in the Symptom Checker.")
            return
        
        # Format datetime
        dt = f"{date} {time}"
        
        # Debug info
        with st.expander("🔍 Debug: Booking Parameters"):
            st.write(f"User ID: {st.session_state['user_id']}")
            st.write(f"Doctor ID: {doctor_id}")
            st.write(f"Symptom ID: {symptom_id}")
            st.write(f"Date/Time: {dt}")
        
        # Book the appointment
        try:
            result = book_appointment(
                st.session_state["user_id"], 
                doctor_id, 
                symptom_id, 
                dt
            )
            
            if result:
                # Simple success message with checkmark in a box
                st.success("✅ Your appointment booked successfully!")
            else:
                st.error("❌ Failed to book appointment. This time slot might already be booked.")
                st.info("Please try selecting a different date or time.")
                
        except Exception as e:
            st.error(f"❌ Error booking appointment: {str(e)}")
            st.exception(e)