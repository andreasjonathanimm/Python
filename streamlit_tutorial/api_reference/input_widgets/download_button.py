import streamlit as st

# Download a large dataframe as a CSV file
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.tocsv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

# Download a string as a file
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

# Download a binary file
binary_contents = b'example content'
# Defaults to 'application/octet-stream'
st.download_button('Download binary file', binary_contents)

# Download an image
with open("flower.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )