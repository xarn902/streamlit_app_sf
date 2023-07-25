import streamlit as st
import pandas as pd

st.title('My Parents New Healthy Diner')
st.header('🐔 🥑🍞Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#selected_fruits = st.multiselect("Pick some fruits: ", list(my_fruit_list['Fruit']))

my_fruit_list = my_fruit_list.set_index('Fruit')
st.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado','Strawberries'])


#my_fruit_list_filtered = my_fruit_list[my_fruit_list['Fruit'].isin(selected_fruits)]

st.dataframe(my_fruit_list)


