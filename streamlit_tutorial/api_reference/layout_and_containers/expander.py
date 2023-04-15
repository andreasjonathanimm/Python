# Warning: Currently, you may not put expanders inside another expander.

# Using "with" notation
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write(\"\"\"
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    \"\"\")
    st.image("https://static.streamlit.io/examples/dice.jpg")

# Call methods directly in the returned objects
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("See explanation")
expander.write(\"\"\"
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
\"\"\")
expander.image("https://static.streamlit.io/examples/dice.jpg")
