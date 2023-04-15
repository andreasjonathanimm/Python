# Important: This is an experimental feature. Experimental features and their APIs are subject to change without notice.

# Rerun the script immediately.

# When st.experimental_rerun() is called, the script is halted - no more statements will be run, and the script will be queued to re-run from the top.

# If this function is called outside of Streamlit, it will raise an Exception.
import streamlit as st

st.experimental_rerun()
