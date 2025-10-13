import pandas as pd
import difflib
import re
 
def _clean(s):
    if s is None:
        return ""
    return re.sub(r'[\s\-_]+', ' ', str(s)).strip().lower()
 
def _find_column(df, candidates):
    cols = [c.lower() for c in df.columns]
    for cand in candidates:
        for i, c in enumerate(cols):
            if cand in c:
                return df.columns[i]
    return None
 
def get_remedies(health_issue, path="data/remedies.csv"):
    try:
        df = pd.read_csv(path, quotechar='"', skipinitialspace=True,
                         engine='python', dtype=str, on_bad_lines='skip', encoding='utf-8')
    except Exception as e:
        print("Error reading CSV:", e)
        return []
 
    if df.shape[0] == 0:
        print("CSV loaded but contains no rows.")
        return []
 
    issue_col = _find_column(df, ["health", "issue", "disease"])
    name_col  = _find_column(df, ["name", "item"])
    remedy_col= _find_column(df, ["remedy", "home"])
 
    if not issue_col:
        print("Could not detect a Health/Issue column. Columns:", df.columns.tolist())
        return []
 
    df["_issue_norm"] = df[issue_col].astype(str).apply(_clean)
    health_issue_clean = _clean(health_issue)
 
    # 1) exact match
    filtered = df[df["_issue_norm"] == health_issue_clean]
 
    # 2) substring contains
    if filtered.empty and health_issue_clean:
        filtered = df[df["_issue_norm"].str.contains(re.escape(health_issue_clean), na=False)]
 
    # 3) fuzzy match
    if filtered.empty:
        unique_issues = df["_issue_norm"].dropna().unique().tolist()
        matches = difflib.get_close_matches(health_issue_clean, unique_issues, n=5, cutoff=0.6)
        if matches:
            filtered = df[df["_issue_norm"].isin(matches)]
 
    remedies = []
    for _, row in filtered.iterrows():
        name_val = row[name_col] if name_col and name_col in row.index else row.get("Name_of_Item", "Unknown")
        remedy_val = row[remedy_col] if remedy_col and remedy_col in row.index else row.get("Home_Remedy", "Not provided")
        remedies.append({
            "name": str(name_val).strip(),
            "issue": str(row.get(issue_col, health_issue)).strip(),
            "remedy": str(remedy_val).strip()
        })
    return remedies
