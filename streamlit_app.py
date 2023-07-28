import streamlit as st
import pandas as pd
import requests
import snowflake.connector




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


st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('what fruit would you like information about?', 'kiwi')
st.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#st.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)




my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows= my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)
