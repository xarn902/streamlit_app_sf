import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError




st.title('My Parents New Healthy Diner')
st.header('🐔 🥑🍞Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie 2')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#selected_fruits = st.multiselect("Pick some fruits: ", list(my_fruit_list['Fruit']))

my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#my_fruit_list_filtered = my_fruit_list[my_fruit_list['Fruit'].isin(selected_fruits)]

st.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('what fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get info")
  else:    
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.error()

st.stop()

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows= my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

add_my_fruit = st.text_input('What fruit would you like to add')
if(add_my_fruit):
  my_cur.execute("INSERT INTO fruit_load_list values('" + add_my_fruit + "')")
  st.write('Thanks for adding '+add_my_fruit)

my_cur.execute("INSERT INTO fruit_load_list values('from streamlit')")

