import streamlit as st
from controllers.symptom_controller import fetch_symptoms, fetch_severity

def render():
    st.title("Symptom Checker")

    if not st.session_state.get("logged_in"):
        st.warning("Please log in to use the symptom checker.")
        st.stop()

    symptoms = fetch_symptoms()
    if not symptoms:
        st.error("No symptoms found. Please check your data file.")
        return

    selected = st.selectbox("Select a symptom", symptoms)

    if st.button("Check Severity"):
        severity = fetch_severity(selected)
        st.session_state["selected_symptom"] = selected
        st.session_state["severity_level"] = severity
        print(selected)
        print(severity)
        st.success(f"Severity level for '{selected}': {severity}")
