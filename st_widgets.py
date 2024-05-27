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

st.divider()

# Slider
x = st.slider('x', value=15, min_value=12, max_value=78, step=3)
st.write(f'x is {x}')

st.divider()

# File Upload
uploaded_file = st.file_uploader('Upload a file:', type=['txt', 'csv', 'xlsx'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == 'text/plain':
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif uploaded_file.type == 'text/csv':
        df = pd.read_csv(uploaded_file)
        st.write(df)
    else:
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df)

st.divider()

# Camera input
camera_photo = st.camera_input('Take a photo')
if camera_photo:
    st.image(camera_photo)

st.image('https://static.streamlit.io/examples/cat.jpg')