# Sidebar
import streamlit as st

my_select_box = st.sidebar.selectbox('Select', ['US', 'UR', 'UK', 'FR'])
my_slider = st.sidebar.slider('Tepmerature')