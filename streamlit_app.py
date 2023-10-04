import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# new code

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What fruit would yo like info about?', 'kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)


    # dataframe will put the info in a table
    # streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()

# Display the table
streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruit_to_show)



# Input 
add_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('The user entered', add_fruit)

# don't run anything past here while we troubleshoot
streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows)

streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

