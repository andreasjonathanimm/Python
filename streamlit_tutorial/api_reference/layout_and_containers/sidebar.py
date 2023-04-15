import streamlit as st
import time

# # Object notation
# st.sidebar.[element_name]

# # "with" notation
# with st.sidebar:
#     st.[element_name]

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

# Important: The only elements that aren't supported using object notation are "st.echo" and "st.spinner". To use these elements, you must use "with" notation.
# How to add st.echo and st.spinner to sidebar:
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")