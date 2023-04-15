import streamlit as st

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric(label="Temperature", value="70 °F", delta="1.2 °F")
col2.metric(label="Wind", value="9 mph", delta="-8%")
col3.metric(label="Humidity", value="86%", delta="4%")

st.metric(label="Gas price", value=4, delta=-0.5, delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123, delta_color="off")