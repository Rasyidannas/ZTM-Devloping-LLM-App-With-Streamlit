# Callback
import streamlit as st
st.subheader('Distance converter')

def miles_to_km():
    # this will update km value when miles is changed
    st.session_state.km = st.session_state.miles * 1.609

def km_to_miles():
    # this will update miles value when km is changed
    st.session_state.miles = st.session_state.km / 1.609

col1, buff, col2 = st.columns([2, 1, 2])
with col1:
    miles = st.number_input('Miles:', key='miles', on_change=miles_to_km)

with col2:
    km = st.number_input('Kilometers:', key='km', on_change=km_to_miles)