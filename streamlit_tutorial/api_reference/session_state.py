import streamlit as st

# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'

# Read
st.write(st.session_state.key)

# Outputs: value

st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API

st.write(st.session_state)

# With magic:
st.session_state


st.write(st.session_state['value'])

# Throws an exception!

# Delete a single key-value pair
del st.session_state[key]

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]

# Session State can also be cleared by going to the Settings menu and clicking "Clear cache"

# Every widget with a key is automatically added to Session State
st.text_input("Your name", key="name")

# This exists now:
st.session_state.name

# Using callbacks to update Session State
# Forms and callbacks
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

# Caveats and limitations
# 1. Only the st.form_submit_button has a callback in forms. Other widgets inside a form are not allowed to have callbacks.
# 2. on_change and on_click events are only supported on input type widgets.
# 3. Modifying the value of a widget via the Session state API, after instantiating it, is not allowed and will raise a StreamlitAPIException. For example:
slider = st.slider(
    label='My Slider', min_value=1,
    max_value=10, value=5, key='my_slider')

st.session_state.my_slider = 7

# Throws an exception!

# Setting the widget state via the Session State API and using the value parameter in the widget declaration is not recommended, and will throw a warning on the first run. For example:
st.session_state.my_slider = 7

slider = st.slider(
    label='Choose a Value', min_value=1,
    max_value=10, value=5, key='my_slider')

# Setting the state of button-like widgets: st.button, st.download_button, and st.file_uploader via the Session State API is not allowed. Such type of widgets are by default False and have ephemeral True states which are only valid for a single run. For example:
if 'my_button' not in st.session_state:
    st.session_state.my_button = True

st.button('My button', key='my_button')

# Throws an exception!
