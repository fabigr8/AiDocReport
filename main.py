
import streamlit as st
from pathlib import Path
from streamlit_extras.switch_page_button import switch_page
import sqlite3
import pandas as pd
import numpy as np



# Connect to the database
conn = sqlite3.connect("database.sqlite")
    
# Create a cursor
c = conn.cursor()



# ####### APP start
# browser info
st.set_page_config(
    page_title="aiDocRep",
    page_icon="⚕️",
)

# Create a title for the app
st.title(":brain: :stethoscope: AI Doc Report ")

# help for the user 
with st.expander("Help"):
        st.write(Path("help.md").read_text())


# form for the customer ID
#with st.form("Search"):
# without form
st.write("### 1. Search for a Patient 🔍 ")
search = st.text_input("Patient ID or patient's family name")
#submitted = st.form_submit_button('Search')

patients = None
df = None

# Search for Patients
if search:
    # get patient data from DB
    with conn:

        # Check the Patient ID
        if search.isnumeric() == True:
            c.execute("SELECT * FROM patients WHERE id = :custid;", {'custid' : search})

        # otherwise maybe family name
        else:
            c.execute("SELECT * FROM patients WHERE nname = :custid;", {'custid' : search})
        
        # Display the fetched patient
        patients = c.fetchall()
    

    if patients is not None:
        st.write("Patient:")
        df = pd.DataFrame(data=patients, columns=('PID','Name', 'Family Name', 'Email'))
        df["ID"] = df["PID"]
        df = df.set_index(['ID'])
        st.table(df)
    else:
        st.write("Patient not found")
    
    
st.write("### 2. Select a single Patient by ID ✅ ")

selected_rows = None
selected_indices = None

# select index from found patients
if df is not None:
    selected_indices = st.multiselect('Select rows:', df.index)

    # if selected get data
    if selected_indices is not None:
        selected_rows = df.loc[selected_indices].copy()
        st.table(selected_rows)




# yes select this patient
if st.button("show details"):
    # next page
    if selected_rows is not None:
        st.session_state['pid'] = selected_rows.index.to_numpy()
        print(selected_rows.values[0])
        switch_page("overview")
    else:
        st.write("please search for a patient id or name")
        #st.write('### Selected Rows', selected_rows)


    