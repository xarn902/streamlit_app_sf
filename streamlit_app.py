import streamlit as st
import pandas as pd

st.title('My Parents New Healthy Diner')
st.header('🐔 🥑🍞Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.text('mango')
st.text('Strawberry')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
