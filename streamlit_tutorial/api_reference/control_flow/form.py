# A form is a container that visually groups other elements and widgets together, and contains a Submit button. When the form's Submit button is pressed, all widget values inside the form will be sent to Streamlit in a batch.

# To add elements to a form object, you can use "with" notation (preferred) or just call methods directly on the form. See examples below.

# Forms have a few constraints:

# 1. Every form must contain a st.form_submit_button.
# 2. st.button and st.download_button cannot be added to a form.
# 3. Forms can appear anywhere in your app (sidebar, columns, etc), but they cannot be embedded inside other forms.

# Inserting elements using "with" notation
import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# Inserting elements out of order
form = st.form("my_form")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")
