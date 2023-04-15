import streamlit as st
import pandas

st.help(pandas.DataFrame)

# Want to quickly check what data type is output by a certain function? Try:
x = my_poorly_documented_function()
st.help(x)

# Want to quickly inspect an object? No sweat:
class Dog:
  '''A typical dog.'''

  def __init__(self, breed, color):
    self.breed = breed
    self.color = color

  def bark(self):
    return 'Woof!'


fido = Dog('poodle', 'white')

st.help(fido)

# And if you're using Magic, you can get help for functions, classes, and modules without even typing "st.help":
import pandas

# Get help for Pandas read_csv:
pandas.read_csv

# Get help for Streamlit itself:
st