# Sidebar
import streamlit as st

my_select_box = st.sidebar.selectbox('Select', ['US', 'UR', 'UK', 'FR'])
my_slider = st.sidebar.slider('Tepmerature')


left_column, right_column = st.columns(2)

import random
data =[random.random() for i in range(100)]

with left_column:
    st.subheader('A linechart')
    st.line_chart(data)

right_column.subheader('Data')
right_column.write(data[:10])

col1, col2, col3 = st.columns([0.2, 0.5, 0.3])

col1.markdown('Hello Streamlit World!!')
col2.write(data[5:10])

with col3:
    st.header('A cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')