import streamlit as st
import pandas as pd
from io import StringIO
st.title("🎈 Welcome to my first :red[Streamlit] App!")
st.write(
    "Upload an image"
)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
   st.image(uploaded_file, caption="MyImage")