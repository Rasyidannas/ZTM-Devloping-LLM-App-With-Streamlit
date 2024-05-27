import streamlit as st
import pandas as pd

# Text Input
name = st.text_input('Your name: ')
if name:
    st.write(f'Hello {name}')

# Number Input
x = st.number_input('Enter a number: ', min_value=1, max_value=99, step=1)
st.write(f'The current number is {x}')

st.divider()

# Button
clicked = st.button('Click me!')
if clicked:
    st.write(':ghost:' * 3)

st.divider()