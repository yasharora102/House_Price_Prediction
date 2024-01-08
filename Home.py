import streamlit as st
from PIL import Image
from decomp import download_files
import os


st.title("Housing Price Prediction of Indian Metro Cities")
st.subheader(
    "Use the sidebar to select the city and other features of the house to predict the price"
)

image = Image.open("house.jpg")
st.image(image, caption="Housing Price Prediction", use_column_width=True)


