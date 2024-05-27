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

# Checkbox
agree = st.checkbox('I agree')
if agree:
    # st.write('Great, you  agreed!')
    'Great, you  agreed!'

checked = st.checkbox('Continue', value=True)
if checked:
    ':+1:' * 5

df = pd.DataFrame({
                    'Name': ['Ciko', 'Ciki', 'Caplin', 'Koski'], 
                    'Age' : [2, 2, 3, 4]
                   })
if st.checkbox('Show data'):
    st.write(df)

st.divider()

# Radio
pets = ['cat', 'dog', 'fish', 'turtle']
pet = st.radio('Favorite pet', pets, index=0, key='your_pet')
st.write(f'Your favorites pet: {pet}')
st.write(f'Your favorites pet: {st.session_state.your_pet * 3}')

st.divider()

# Select
cities = ['London', 'Jakarta', 'Paris', 'Berlin']
city = st.selectbox('Your city', cities, index=1)
st.write(f'You life in {city}')