import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

# Read the image file buffer as bytes
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))

# IMPORTANT: st.camera_input returns an object of the UploadedFile class, which a subclass of BytesIO. Therefore it is a "file-like" object. This means you can pass it anywhere where a file is expected, similar to st.file_uploader.