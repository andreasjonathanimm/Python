import streamlit as st
from transformers import BertModel

@st.cache_resource
 def get_database_session(url):
     # Create a database session object that points to the URL.
     return session

@st.cache_resource
def get_model(model_type):
    # Create a model of the specified type.
    return BertModel.from_pretrained(model_type)

if st.button("Clear All"):
    # Clears all st.cache_resource caches:
    st.cache_resource.clear()