

import streamlit as st
from pathlib import Path

# ############# browser info
st.set_page_config(
    page_title="aiDocRep",
    page_icon="⚕️",
)



# ##### sidepannel
# Create a side panel
st.sidebar.title("Settings")
# Create a slider
slider = st.sidebar.slider("Slider", 0, 100, 50)
# Create a checkbox
checkbox = st.sidebar.checkbox("Checkbox")
# Create a dropdown
dropdown = st.sidebar.selectbox("Dropdown", ["Option 1", "Option 2", "Option 3"])

# Display the values of the slider, checkbox, and dropdown
st.write("Slider value:", slider)
st.write("Checkbox value:", checkbox)
st.write("Dropdown value:", dropdown)