import streamlit
import pandas

# streamlit.header('Breakfast Menu')
# streamlit.text('Omega 3 & Blueberry Oatmeal')
# streamlit.text('Kale, Spinach & Rocket Smoothie')
# streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Pick up the fruit they want to include
stramlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

# Display the table
streamlit.dataframe(my_fruit_list)

