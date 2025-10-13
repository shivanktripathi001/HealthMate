import pandas as pd
from functools import lru_cache
import os
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
 
@lru_cache(maxsize=1)
def load_symptoms():
    path = os.path.join(DATA_DIR, "symptoms.csv")
    return pd.read_csv(path)
 
@lru_cache(maxsize=1)
def load_severity():
    path = os.path.join(DATA_DIR, "severity.csv")
    return pd.read_csv(path)
 
def get_symptom_list():
    df = load_symptoms()
    # Corrected: Using 'Diseases' to match the column name in the CSV
    return df["Diseases"].dropna().unique().tolist() 
 
def get_severity(symptom_name):
    df = load_severity()
    match = df[df["Symptom"] == symptom_name]
    return match["weight"].values[0] if not match.empty else "Unknown"
 
def get_symptom_id_by_name(symptom_name):
    df = load_symptoms()
    # Corrected: Using 'Diseases' to match the column name in the CSV
    match = df[df["Diseases"] == symptom_name] 
    return match["symptom_id"].values[0] if not match.empty else None
 