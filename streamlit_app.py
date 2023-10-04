import streamlit
import pandas
import requests
import snowflake.connector



# streamlit.header('Breakfast Menu')
# streamlit.text('Omega 3 & Blueberry Oatmeal')
# streamlit.text('Kale, Spinach & Rocket Smoothie')
# streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# # Pick up the fruit they want to include by fruit name
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries','Banana'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]

# Input 
fruit_choice = streamlit.text_input('What fruit would yo like info about?', 'kiwi')
streamlit.write('The user entered', fruit_choice)


# Display the table
streamlit.dataframe(my_fruit_list)
# streamlit.dataframe(fruit_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# dataframe will put the info in a table
streamlit.dataframe(fruityvice_normalized)

# Input 
add_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('The user entered', add_fruit)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

