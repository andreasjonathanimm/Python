import streamlit as st

@st.cache_resource
def get_database_session(url):
    # Create a database session object that points to the URL.
    return session

s1 = get_database_session(SESSION_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

s2 = get_database_session(SESSION_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the connection object in s1 is the same as in s2.

s3 = get_database_session(SESSION_URL_2)
# This is a different URL, so the function executes.

# By default, all parameters to a cache_resource function must be hashable. Any parameter whose name begins with _ will not be hashed. You can use this as an "escape hatch" for parameters that are not hashable:
import streamlit as st

@st.cache_resource
def get_database_session(_sessionmaker, url):
    # Create a database connection object that points to the URL.
    return connection

s1 = get_database_session(create_sessionmaker(), DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

s2 = get_database_session(create_sessionmaker(), DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value - even though the _sessionmaker parameter was different
# in both calls.

# A cache_resource function's cache can be procedurally cleared:
@st.cache_resource
def get_database_session(_sessionmaker, url):
    # Create a database connection object that points to the URL.
    return connection

get_database_session.clear()
# Clear all cached entries for this function.


# Static elements
from transformers import pipeline

@st.cache_resource
def load_model():
    model = pipeline("sentiment-analysis")
    st.success("Loaded NLP model from Hugging Face!")  # 👈 Show a success message
    return model

# You can also use this functionality to cache entire parts of your UI:
@st.cache_resource
def load_model():
    st.header("Data analysis")
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT)
    st.success("Loaded model!")
    st.write("Turning on evaluation mode...")
    model.eval()
    st.write("Here's the model:")
    return model

# Input widgets
# You can also use interactive input widgets like st.slider or st.text_input in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the experimental_allow_widgets parameter:
@st.cache_data(experimental_allow_widgets=True)  # 👈 Set the parameter
def load_model():
    pretrained = st.checkbox("Use pre-trained model:")  # 👈 Add a checkbox
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT, pretrained=pretrained)
    return model

# Warning: Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!

# Note: Two widgets are currently not supported in cached functions: st.file_uploader and st.camera_input. We may support them in the future. Feel free to open a GitHub issue if you need them!
