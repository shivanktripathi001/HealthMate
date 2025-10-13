import pandas as pd
 
def remedy_generator(health_issue):
    try:
        # Load and clean the CSV
        df = pd.read_csv("data/remedies.csv", quotechar='"', on_bad_lines='skip')
        df.columns = df.columns.str.strip()  # Clean column names
 
        # Normalize the health issue for matching
        df["Health_Issue"] = df["Health_Issue"].astype(str).str.strip().str.lower()
        health_issue = str(health_issue).strip().lower()
 
        # Filter remedies
        filtered = df[df["Health_Issue"] == health_issue]
 
        # Yield results
        for _, row in filtered.iterrows():
            yield {
                "name": row.get("Name_of_Item", "Unknown"),
                "issue": row.get("Health_Issue", health_issue),
                "remedy": row.get("Home_Remedy", "Not provided"),
            }
 
    except Exception as e:
        print("Error loading remedies:", e)
        return []