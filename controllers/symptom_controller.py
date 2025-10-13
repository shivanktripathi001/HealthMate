from models.symptom_model import get_symptom_list, get_severity, get_symptom_id_by_name

def fetch_symptoms():
    return get_symptom_list()

def fetch_severity(symptom):
    return get_severity(symptom)

def get_symptom_id(symptom_name):
    return get_symptom_id_by_name(symptom_name)
