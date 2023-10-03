import streamlit
import pandas
import requests



# streamlit.header('Breakfast Menu')
# streamlit.text('Omega 3 & Blueberry Oatmeal')
# streamlit.text('Kale, Spinach & Rocket Smoothie')
# streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# # Pick up the fruit they want to include by fruit name
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries','Banana'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table
streamlit.dataframe(my_fruit_list)
# streamlit.dataframe(fruit_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

