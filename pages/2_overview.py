import streamlit as st
from pathlib import Path
import sqlite3


# ############# browser info
st.set_page_config(
    page_title="aiDocRep",
    page_icon="⚕️",
)

# ######### DB 
# Connect to the database
conn = sqlite3.connect("database.sqlite")
    
# Create a cursor
c = conn.cursor()


patient_id = None

# get Patient Data from DB
if 'pid' not in st.session_state:
    st.write("no patient given, please go back and select a patient")
else:
    patient_id = st.session_state['pid']


#show patient details
if patient_id is not None:
    with conn:
        # get the Patient Data
        c.execute("SELECT * FROM patients WHERE id = :pid;", {'pid' : patient_id[0].astype(str)})
        # get the Patient Data
        patient = c.fetchone()

    if patient is not None:
        st.write("Patiend ID:", patient[0])
        st.write("Name ID:", patient[1])
        st.write("Family Name ID:", patient[2])
        st.write("Patient Mail:", patient[3])
    else:
        st.write("Patient not found")






#show document overview of patients stay

# --> get doc ID, Title, and Date from Metadata.

