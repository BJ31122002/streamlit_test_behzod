import streamlit as st

st.title('Test app')

st.write('Hello world!')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')\
print(df)
