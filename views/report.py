# import streamlit as st
# from controllers.report_controller import save_report, fetch_reports
 
# def render():
#     st.subheader(" Patient Report")
 
#     if not st.session_state.get("logged_in"):
#         st.warning("Please log in first.")
#         return
 
#     with st.form("report_form"):
#         patient_name = st.text_input("Patient Name")
#         age = st.number_input("Age", min_value=0, max_value=120)
#         diagnosis = st.text_area("Diagnosis")
#         prescription = st.text_area("Prescription")
#         notes = st.text_area("Additional Notes")
#         submitted = st.form_submit_button("Save Report")
 
#     if submitted:
#         success = save_report(
#             st.session_state["username"],
#             patient_name,
#             age,
#             diagnosis,
#             prescription,
#             notes
#         )
#         if success:
#             st.success(" Report saved successfully!")
#         else:
#             st.error(" Failed to save report.")
 
#     st.markdown("###  Your Reports")
#     reports = fetch_reports(st.session_state["username"])
#     for report in reports:
#         st.markdown("---")
#         st.markdown(f"**Patient:** {report['patient_name']} | Age: {report['age']}")
#         st.markdown(f"**Diagnosis:** {report['diagnosis']}")
#         st.markdown(f"**Prescription:** {report['prescription']}")
#         st.markdown(f"**Notes:** {report['notes']}")


# report.py
# import streamlit as st
# from controllers.report_controller import save_report, fetch_reports

# def render():
#     st.subheader("📋 Patient Report")

#     if not st.session_state.get("logged_in"):
#         st.warning("Please log in first.")
#         return

#     with st.form("report_form"):
#         patient_name = st.text_input("Patient Name", placeholder="Enter patient's full name")
#         age = st.number_input("Age", min_value=0, max_value=120, value=0)
#         diagnosis = st.text_area("Diagnosis", placeholder="Enter diagnosis details")
#         prescription = st.text_area("Prescription", placeholder="Enter prescription details")
#         notes = st.text_area("Additional Notes", placeholder="Any additional notes")
#         submitted = st.form_submit_button("💾 Save Report")

#     if submitted:
#         # Validate required fields
#         if not patient_name or not diagnosis or not prescription:
#             st.error("❌ Please fill in all required fields: Patient Name, Diagnosis, and Prescription")
#             return
            
#         success = save_report(
#             st.session_state["username"],
#             patient_name,
#             age,
#             diagnosis,
#             prescription,
#             notes
#         )
#         if success:
#             st.success("✅ Report saved successfully!")
#             st.rerun()  # Refresh to show the new report
#         else:
#             st.error("❌ Failed to save report. Please check the console for details.")

#     # Display existing reports
#     st.markdown("### 📄 Your Reports")
#     reports = fetch_reports(st.session_state["username"])
    
#     if not reports:
#         st.info("No reports found. Create your first report above!")
#     else:
#         for report in reports:
#             st.markdown("---")
#             st.markdown(f"**Patient:** {report.get('patient_name', 'N/A')} | **Age:** {report.get('age', 'N/A')}")
#             st.markdown(f"**Diagnosis:** {report.get('diagnosis', 'N/A')}")
#             st.markdown(f"**Prescription:** {report.get('prescription', 'N/A')}")
#             if report.get('notes'):
#                 st.markdown(f"**Notes:** {report.get('notes', 'N/A')}")
#             st.markdown(f"*Created on:* {report.get('created_at', 'N/A')}")
 

# report.py
import streamlit as st
from controllers.report_controller import save_report, fetch_reports

def render():
    st.subheader("📋 Patient Report")

    if not st.session_state.get("logged_in"):
        st.warning("Please log in first.")
        return

    with st.form("report_form"):
        patient_name = st.text_input("Patient Name*", placeholder="Enter patient's full name")
        age = st.number_input("Age*", min_value=0, max_value=120, value=30)
        diagnosis = st.text_area("Diagnosis*", placeholder="Enter diagnosis details")
        prescription = st.text_area("Prescription*", placeholder="Enter prescription details")
        notes = st.text_area("Additional Notes", placeholder="Any additional notes (optional)")
        submitted = st.form_submit_button("💾 Save Report")

    if submitted:
        # Validate required fields
        if not patient_name.strip():
            st.error("❌ Patient Name is required")
            return
        if not diagnosis.strip():
            st.error("❌ Diagnosis is required")
            return
        if not prescription.strip():
            st.error("❌ Prescription is required")
            return
        if age <= 0:
            st.error("❌ Please enter a valid age")
            return
            
        # Show processing message
        with st.spinner("Saving report..."):
            success = save_report(
                st.session_state["username"],
                patient_name.strip(),
                age,
                diagnosis.strip(),
                prescription.strip(),
                notes.strip()
            )
        
        if success:
            st.success("✅ Report saved successfully!")
            st.balloons()
            # Wait a moment before rerun
            import time
            time.sleep(1)
            st.rerun()
        else:
            st.error("❌ Failed to save report. Please check the console for details.")
            st.info("💡 Tip: Make sure your database connection is working and the reports table exists.")

    # Display existing reports
    st.markdown("---")
    st.markdown("### 📄 Your Reports")
    
    with st.spinner("Loading reports..."):
        reports = fetch_reports(st.session_state["username"])
    
    if not reports:
        st.info("📭 No reports found. Create your first report above!")
    else:
        st.success(f"Found {len(reports)} report(s)")
        
        for idx, report in enumerate(reports, 1):
            with st.expander(f"📌 Report #{idx} - {report.get('patient_name', 'N/A')}", expanded=(idx==1)):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Patient:** {report.get('patient_name', 'N/A')}")
                    st.markdown(f"**Age:** {report.get('age', 'N/A')} years")
                with col2:
                    st.markdown(f"**Report ID:** {report.get('report_id', 'N/A')}")
                    st.markdown(f"**Created:** {report.get('created_at', 'N/A')}")
                
                st.markdown("---")
                st.markdown(f"**🔍 Diagnosis:**")
                st.info(report.get('diagnosis', 'N/A'))
                
                st.markdown(f"**💊 Prescription:**")
                st.success(report.get('prescription', 'N/A'))
                
                if report.get('notes'):
                    st.markdown(f"**📝 Additional Notes:**")
                    st.warning(report.get('notes', 'N/A'))