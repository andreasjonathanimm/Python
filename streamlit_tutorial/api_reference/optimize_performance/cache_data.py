import streamlit as st

@st.cache_data
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data

d1 = fetch_and_clean_data(DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

d2 = fetch_and_clean_data(DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the data in d1 is the same as in d2.

d3 = fetch_and_clean_data(DATA_URL_2)
# This is a different URL, so the function executes.

# To set the "persist" parameter, use this command as follows:
@st.cache_data(persist="disk")
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data

# By default, all parameters to a cached function must be hashable. Any parameter whose name begins with _ will not be hashed. You can use this as an "escape hatch" for parameters that are not hashable:
@st.cache_data
def fetch_and_clean_data(_db_connection, num_rows):
    # Fetch data from _db_connection here, and then clean it up.
    return data

connection = make_database_connection()
d1 = fetch_and_clean_data(connection, num_rows=10)
# Actually executes the function, since this is the first time it was
# encountered.

another_connection = make_database_connection()
d2 = fetch_and_clean_data(another_connection, num_rows=10)
# Does not execute the function. Instead, returns its previously computed
# value - even though the _database_connection parameter was different
# in both calls.

# A cached function's cache can be procedurally cleared:
import streamlit as st

@st.cache_data
def fetch_and_clean_data(_db_connection, num_rows):
    # Fetch data from _db_connection here, and then clean it up.
    return data

fetch_and_clean_data.clear()
# Clear all cached entries for this function.


# Static elements
@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # 👈 Show a success message
    return data

# As we know, Streamlit only runs this function if it hasn’t been cached before. On this first run, the st.success message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an st. command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

# You can also use this functionality to cache entire parts of your UI:
@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)


# Input widgets
# You can also use interactive input widgets like st.slider or st.text_input in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the experimental_allow_widgets parameter:
@st.cache_data(experimental_allow_widgets=True)  # 👈 Set the parameter
def get_data():
    num_rows = st.slider("Number of rows to get")  # 👈 Add a slider
    data = api.get(..., num_rows)
    return data

# Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then we’ll add 100 MB to the cache for every permutation of these five slider values – even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

# Warning: Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!

# Note: Two widgets are currently not supported in cached functions: st.file_uploader and st.camera_input. We may support them in the future. Feel free to open a GitHub issue if you need them!