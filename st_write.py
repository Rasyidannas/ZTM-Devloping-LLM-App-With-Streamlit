import streamlit as st
import pandas as pd

st.title('Hello Straemlit World! :100:')

# Displaying data on the screen
# using st.write()
st.write('We learn Streamlit!')
l1 = [1,2,3]
st.write(l1)

ls = list('abc')
d1 = dict(zip(l1, ls))
st.write(d1)

# using magic
'Displaying using magic :smile:'

df = pd.DataFrame({
    'first_column': [1,2,3,4],
    'second_column': [10,20,30,40]
})
# this is same like st.write(df)
df