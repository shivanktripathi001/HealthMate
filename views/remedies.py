# import streamlit as st
# from controllers.remedy_controller import get_remedies

# def render():
#     st.title("Remedies")

#     symptom = st.session_state.get("selected_symptom", None)

#     if not symptom:
#         st.warning("Please check a symptom first.")
#     else:
#         remedies = get_remedies(symptom)
#         for remedy in remedies:
#             st.subheader(remedy["Home Remedy"])
#             st.markdown(f"Ingredients: {remedy['Home Remedy']}")
#             st.markdown("---")

# import streamlit as st
# from controllers.remedy_controller import get_remedies
 
# def render():
#     st.title("Remedies")
    
#     symptom = st.session_state.get("selected_symptom", None)
    
#     if not symptom:
#         st.warning("Please check a symptom first.")
#     else:
#         remedies = get_remedies(symptom)
        
#         if not remedies:
#             st.info("No remedies found for this symptom.")
        
#         for remedy in remedies:
#             st.subheader(remedy["name"])  # Show Name of Item
#             st.markdown(f"**Remedy:** {remedy['remedy']}")  # Show Home Remedy
#             st.markdown("---")




# import streamlit as st
# from controllers.remedy_controller import get_remedies
 
# def render():
#     st.title("Remedies")
    
#     # Get selected symptom from session state
#     symptom = st.session_state.get("selected_symptom", None)
    
#     if not symptom:
#         st.warning("Please check a symptom first.")
#         return
    
#     # Get remedies for the symptom
#     remedies = get_remedies(symptom)
    
#     if not remedies:
#         st.info("No remedies found for this symptom.")
#         return
    
#     # Display each remedy
#     for remedy in remedies:
#         st.subheader(remedy["name"])  # Show Name of Item
#         st.markdown(f"**Remedy:** {remedy['remedy']}")  # Show Home Remedy
#         st.markdown("---")


#Run thi one 
# import streamlit as st
# from controllers.remedy_controller import get_remedies

# def render():
#     st.title("Remedies")

#     # Get selected symptom from session state
#     symptom = st.session_state.get("selected_symptom", None)

#     if not symptom:
#         st.warning("Please check a symptom first.")
#         return

#     # Get remedies for the symptom
#     remedies = get_remedies(symptom)

#     if not remedies:
#         st.info("No remedies found for this symptom.")
#         return

#     # Display each remedy
#     for remedy in remedies:
#         st.subheader(remedy.get("name", "Unknown Item"))
#         st.markdown(f"**Health Issue:** {remedy.get('issue', symptom)}")
#         st.markdown(f"**Home Remedy:** {remedy.get('remedy', 'Not provided')}")

#         yogasan_url = remedy.get("yogasan", "").strip()
#         if yogasan_url:
#             st.image(yogasan_url, caption="Recommended Yogasan", use_column_width=True)
#         else:
#             st.markdown("_No Yogasan image available._")

#         st.markdown("---")






# import streamlit as st
# from controllers.remedy_controller import get_remedies
# import pandas as pd
# import re
 
# st.set_page_config(page_title="Remedies", layout="wide")
 
# def render():
#     st.title("Remedies")
 
#     # Allow override for testing: either use session state (from symptom checker) or manual input
#     symptom_from_state = st.session_state.get("selected_symptom", None)
#     st.markdown(f"**Debug — session selected_symptom:** `{symptom_from_state}`")
 
#     test_input = st.text_input("Type a symptom to test (e.g. malaria, allergy) — this overrides session value:", value="")
#     symptom = test_input.strip() or symptom_from_state
 
#     if not symptom:
#         st.warning("No symptom provided. Either set `st.session_state['selected_symptom']` in your app, or type a symptom above to test.")
#         return
 
#     st.markdown(f"**Searching remedies for:** `{symptom}`")
 
#     remedies = get_remedies(symptom)
 
#     if not remedies:
#         st.info("No remedies found for this symptom. Below are CSV diagnostics:")
 
#         try:
#             df = pd.read_csv("data/remedies.csv", quotechar='"', skipinitialspace=True,
#                              engine='python', dtype=str, on_bad_lines='skip', encoding='utf-8')
#             issue_cols = [c for c in df.columns if re.search(r'health|issue|dise', c, re.I)]
#             if issue_cols:
#                 col = issue_cols[0]
#                 st.markdown("**Available health issues in CSV (sample 100 unique):**")
#                 vals = pd.Series(df[col].astype(str).str.strip().dropna().unique()).head(100).tolist()
#                 st.write(vals)
#             else:
#                 st.write("Couldn't find an issue-like column in CSV. Columns are:", df.columns.tolist())
#         except Exception as e:
#             st.write("Couldn't read CSV for debug:", e)
#         return
 
#     for r in remedies:
#         st.subheader(r.get("name", "Unknown Item"))
#         st.markdown(f"**Health Issue:** {r.get('issue')}")
#         st.markdown(f"**Home Remedy:** {r.get('remedy')}")
#         st.markdown("---")
 
# if __name__ == "__main__":
#     render()










# import streamlit as st
# from controllers.remedy_controller import get_remedies
# import pandas as pd
# import re
 
# # Set page configuration for wider layout
# st.set_page_config(page_title="Remedies", layout="wide")
 
# def render():
#     st.title("Home Remedies") # Changed title for consistency, you can adjust
 
#     # Retrieve symptom from session state (expected from symptom checker)
#     symptom_from_state = st.session_state.get("selected_symptom", None)
#     st.markdown(f"**Debug — session selected_symptom:** `{symptom_from_state}`")
 
#     # Allow manual input for testing, which overrides the session state value
#     test_input = st.text_input("Type a symptom to test (e.g. malaria, allergy) — this overrides session value:", value="")
    
#     # Determine the symptom to use: manual input if provided, otherwise from session state
#     symptom_to_process = test_input.strip() or symptom_from_state
 
#     if not symptom_to_process:
#         st.warning("No symptom provided. Please navigate to the 'Symptom Checker' first, or type a symptom above to test.")
#         return
 
#     st.markdown(f"**Searching remedies for:** `{symptom_to_process}`")
 
#     # Get remedies using the controller
#     remedies = get_remedies(symptom_to_process)
 
#     if not remedies:
#         st.info(f"No remedies found for '{symptom_to_process}'. Below are CSV diagnostics:")
#         try:
#             # Attempt to load and display a sample of available health issues from the CSV
#             # Using encoding='utf-8-sig' for robustness against BOM
#             df = pd.read_csv("data/remedies.csv", quotechar='"', skipinitialspace=True, engine='python', dtype=str, on_bad_lines='skip', encoding='utf-8-sig')
            
#             # Identify columns that likely contain health issues
#             issue_cols = [c for c in df.columns if re.search(r'health|issue|dise', c, re.I)]
            
#             if issue_cols:
#                 col = issue_cols[0] # Take the first identified issue column
#                 st.markdown("**Available health issues in CSV (sample 100 unique, normalized):**")
                
#                 # Apply the same cleaning/normalization as the controller for comparison
#                 from controllers.remedy_controller import _clean_text # Import the cleaning function
#                 normalized_vals = pd.Series(df[col].astype(str).apply(_clean_text).dropna().unique()).head(100).tolist()
#                 st.code("\n".join(normalized_vals)) # Use st.code for better readability of the list
#                 if len(pd.Series(df[col].astype(str).apply(_clean_text).dropna().unique()).tolist()) > 100:
#                     st.markdown("*(... more issues available ...)*")
#             else:
#                 st.markdown("Couldn't find an issue-like column in `remedies.csv` for debugging.")
#                 st.code(f"Detected columns: {df.columns.tolist()}")
#         except FileNotFoundError:
#             st.error("Error: `remedies.csv` not found at `data/remedies.csv`. Please ensure the file exists.")
#         except Exception as e:
#             st.error(f"Error loading `remedies.csv` for debug display: `{e}`")
#         return
 
#     # Display found remedies
#     for remedy_item in remedies:
#         with st.container():
#             st.markdown("---") # Separator for each remedy
#             st.markdown(f"#### {remedy_item.get('name', 'Unknown Item')}")
#             st.markdown(f"**Health Issue:** {remedy_item.get('issue', symptom_to_process)}")
#             st.markdown(f"**Home Remedy:** {remedy_item.get('remedy', 'Not provided')}")
#             # Add a small image to visualize the section (example)
#             # You can customize this or remove if not needed
#             # For demonstration purposes, I'm adding a generic image.
#             # You would replace 'https://via.placeholder.com/150' with a relevant icon/image URL
#             # st.image('https://via.placeholder.com/150', caption='Remedy Icon', width=80)
            
# # This block ensures that render() is called when the script is run directly
# if __name__ == "__main__":
#     render()


# import streamlit as st
# from controllers.remedy_controller import _clean_text
# import pandas as pd
# import re
 
# # Set page configuration for wider layout
# st.set_page_config(page_title="Remedies", layout="wide")
 
# def render():
#     st.title("Home Remedies") # Changed title for consistency, you can adjust
 
#     # Retrieve symptom from session state (expected from symptom checker)
#     symptom_from_state = st.session_state.get("selected_symptom", None)
    
#     # Keeping the sidebar debug print, but you can remove this line too if desired
#     st.sidebar.markdown(f"**Debug — session selected_symptom:** `{symptom_from_state}`")
 
#     # Use the symptom directly from session state
#     symptom_to_process = symptom_from_state
 
#     if not symptom_to_process:
#         st.warning("No symptom provided. Please navigate to the 'Symptom Checker' first and select a symptom.")
#         return
 
#     st.subheader(f"Remedies for: {symptom_to_process}") # Changed to subheader for better hierarchy
 
#     # Get remedies using the controller
#     remedies = get_remedies(symptom_to_process)
 
#     if not remedies:
#         st.info(f"No remedies found for '{symptom_to_process}'. Below are CSV diagnostics:")
#         try:
#             # Attempt to load and display a sample of available health issues from the CSV
#             df = pd.read_csv("data/remedies.csv", quotechar='"', skipinitialspace=True, engine='python', dtype=str, on_bad_lines='skip', encoding='utf-8-sig')
            
#             # Identify columns that likely contain health issues
#             issue_cols = [c for c in df.columns if re.search(r'health|issue|dise', c, re.I)]
            
#             if issue_cols:
#                 col = issue_cols[0] # Take the first identified issue column
#                 st.markdown("**Available health issues in CSV (sample 100 unique, normalized):**")
                
#                 # Apply the same cleaning/normalization as the controller for comparison
#                 from controllers.remedy_controller import _clean_text # Import the cleaning function
#                 normalized_vals = pd.Series(df[col].astype(str).apply(_clean_text).dropna().unique()).head(100).tolist()
#                 st.code("\n".join(normalized_vals)) # Use st.code for better readability of the list
#                 if len(pd.Series(df[col].astype(str).apply(_clean_text).dropna().unique()).tolist()) > 100:
#                     st.markdown("*(... more issues available ...)*")
#             else:
#                 st.markdown("Couldn't find an issue-like column in `remedies.csv` for debugging.")
#                 st.code(f"Detected columns: {df.columns.tolist()}")
#         except FileNotFoundError:
#             st.error("Error: `remedies.csv` not found at `data/remedies.csv`. Please ensure the file exists.")
#         except Exception as e:
#             st.error(f"Error loading `remedies.csv` for debug display: `{e}`")
#         return
 
#     # Display found remedies
#     for remedy_item in remedies:
#         with st.container():
#             st.markdown("---") # Separator for each remedy
#             st.markdown(f"#### {remedy_item.get('name', 'Unknown Item')}")
#             st.markdown(f"**Health Issue:** {remedy_item.get('issue', symptom_to_process)}")
#             st.markdown(f"**Home Remedy:** {remedy_item.get('remedy', 'Not provided')}")
            
# # This block ensures that render() is called when the script is run directly
# if __name__ == "__main__":
#     render()


import streamlit as st
from controllers.remedy_controller import get_remedies, _clean # Added _clean to the import
import pandas as pd
import re
 
# Set page configuration for wider layout
st.set_page_config(page_title="Remedies", layout="wide")
 
def render():
    st.title("Home Remedies") # Changed title for consistency, you can adjust
    
    # Retrieve symptom from session state (expected from symptom checker)
    symptom_from_state = st.session_state.get("selected_symptom", None)
    
    # Keeping the sidebar debug print, but you can remove this line too if desired
    st.sidebar.markdown(f"**Debug — session selected_symptom:** `{symptom_from_state}`")
 
    # Use the symptom directly from session state
    symptom_to_process = symptom_from_state
    if not symptom_to_process:
        st.warning("No symptom provided. Please navigate to the 'Symptom Checker' first and select a symptom.")
        return
 
    st.subheader(f"Remedies for: {symptom_to_process}") # Changed to subheader for better hierarchy
 
    # Get remedies using the controller
    remedies = get_remedies(symptom_to_process)
 
    if not remedies:
        st.info(f"No remedies found for '{symptom_to_process}'. Below are CSV diagnostics:")
        try:
            # Attempt to load and display a sample of available health issues from the CSV
            df = pd.read_csv("data/remedies.csv", quotechar='"', skipinitialspace=True, engine='python', dtype=str, on_bad_lines='skip', encoding='utf-8-sig')
            
            # Identify columns that likely contain health issues
            issue_cols = [c for c in df.columns if re.search(r'health|issue|dise', c, re.I)]
            
            if issue_cols:
                col = issue_cols[0] # Take the first identified issue column
                st.markdown("**Available health issues in CSV (sample 100 unique, normalized):**")
                
                # Apply the same cleaning/normalization as the controller for comparison
                normalized_vals = pd.Series(df[col].astype(str).apply(_clean).dropna().unique()).head(100).tolist() # Used _clean instead of _clean_text
                st.code("\n".join(normalized_vals)) # Use st.code for better readability of the list
                
                if len(pd.Series(df[col].astype(str).apply(_clean).dropna().unique()).tolist()) > 100:
                    st.markdown("*(... more issues available ...)*")
            else:
                st.markdown("Couldn't find an issue-like column in `remedies.csv` for debugging.")
                st.code(f"Detected columns: {df.columns.tolist()}")
 
        except FileNotFoundError:
            st.error("Error: `remedies.csv` not found at `data/remedies.csv`. Please ensure the file exists.")
        except Exception as e:
            st.error(f"Error loading `remedies.csv` for debug display: `{e}`")
        return
        
    # Display found remedies
    for remedy_item in remedies:
        with st.container():
            st.markdown("---") # Separator for each remedy
            st.markdown(f"#### {remedy_item.get('name', 'Unknown Item')}")
            st.markdown(f"**Health Issue:** {remedy_item.get('issue', symptom_to_process)}")
            st.markdown(f"**Home Remedy:** {remedy_item.get('remedy', 'Not provided')}")
 
# This block ensures that render() is called when the script is run directly
if __name__ == "__main__":
    render()





