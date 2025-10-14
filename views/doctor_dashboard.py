import streamlit as st
from controllers.doctor_controller import fetch_hospital_appointments, change_appointment_status
import pandas as pd
from datetime import datetime

def render():
    if not st.session_state.get("doctor_logged_in"):
        st.warning("Please log in as a doctor to access this page.")
        st.stop()
    
    # Header
    st.title(" Doctor Admin Dashboard")
    st.markdown(f"**Welcome, Dr. {st.session_state.get('doctor_name')}**")
    st.markdown(f"*Specialization: {st.session_state.get('doctor_specialization')}*")
    st.markdown("---")
    
    # Logout button
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("Logout"):
            st.session_state.doctor_logged_in = False
            st.session_state.page = "Doctor Login"
            st.rerun()
    
    # Fetch appointments
    hospital_id = st.session_state.get("doctor_hospital_id")
    appointments = fetch_hospital_appointments(hospital_id)
    
    if not appointments:
        st.info("No appointments found for your hospital.")
        return
    
    # Statistics
    st.subheader("📊 Appointment Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    total_appointments = len(appointments)
    pending = sum(1 for a in appointments if a['status'] == 'pending')
    confirmed = sum(1 for a in appointments if a['status'] == 'confirmed')
    completed = sum(1 for a in appointments if a['status'] == 'completed')
    
    col1.metric("Total Appointments", total_appointments)
    col2.metric("Pending", pending, delta=None)
    col3.metric("Confirmed", confirmed, delta=None)
    col4.metric("Completed", completed, delta=None)
    
    st.markdown("---")
    
    # Filter options
    st.subheader("🔍 Filter Appointments")
    filter_col1, filter_col2 = st.columns(2)
    
    with filter_col1:
        status_filter = st.selectbox(
            "Filter by Status",
            ["All", "pending", "confirmed", "completed", "cancelled"]
        )
    
    with filter_col2:
        date_filter = st.date_input("Filter by Date (optional)")
    
    # Apply filters
    filtered_appointments = appointments
    if status_filter != "All":
        filtered_appointments = [a for a in filtered_appointments if a['status'] == status_filter]
    
    st.markdown("---")
    
    # Display appointments
    st.subheader("📋 Appointment Details")
    
    if not filtered_appointments:
        st.warning("No appointments match the selected filters.")
    else:
        for idx, appointment in enumerate(filtered_appointments):
            with st.expander(
                f"Appointment #{appointment['appointment_id']} - {appointment['patient_name']} - {appointment['appointment_date']} - Status: {appointment['status'].upper()}"
            ):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Patient Information:**")
                    st.write(f"👤 Name: {appointment['patient_name']}")
                    st.write(f"📧 Email: {appointment['patient_email']}")
                    st.write(f"📅 Appointment Date: {appointment['appointment_date']}")
                
                with col2:
                    st.write("**Medical Information:**")
                    st.write(f"🏥 Hospital: {appointment['hospital_name']}")
                    st.write(f"🩺 Symptom: {appointment['symptom_name']}")
                    st.write(f"📝 Description: {appointment['symptom_description']}")
                
                st.markdown("---")
                
                # Status update
                st.write("**Update Status:**")
                status_col1, status_col2, status_col3, status_col4 = st.columns(4)
                
                with status_col1:
                    if st.button("✅ Confirm", key=f"confirm_{appointment['appointment_id']}"):
                        if change_appointment_status(appointment['appointment_id'], 'confirmed'):
                            st.success("Status updated to Confirmed!")
                            time.sleep(1)
                            st.rerun()
                
                with status_col2:
                    if st.button("✔️ Complete", key=f"complete_{appointment['appointment_id']}"):
                        if change_appointment_status(appointment['appointment_id'], 'completed'):
                            st.success("Status updated to Completed!")
                            time.sleep(1)
                            st.rerun()
                
                with status_col3:
                    if st.button("❌ Cancel", key=f"cancel_{appointment['appointment_id']}"):
                        if change_appointment_status(appointment['appointment_id'], 'cancelled'):
                            st.warning("Appointment Cancelled!")
                            time.sleep(1)
                            st.rerun()
                
                with status_col4:
                    if st.button("⏳ Pending", key=f"pending_{appointment['appointment_id']}"):
                        if change_appointment_status(appointment['appointment_id'], 'pending'):
                            st.info("Status updated to Pending!")
                            time.sleep(1)
                            st.rerun()
    
    # Download as CSV
    st.markdown("---")
    if st.button("📥 Download Appointments as CSV"):
        df = pd.DataFrame(filtered_appointments)
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"appointments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )