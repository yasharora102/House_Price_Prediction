import streamlit as st
from PIL import Image
from streamlit_extras.app_logo import add_logo
from pathlib import Path
import base64


st.set_page_config(
    layout="wide",
    page_title="House Price Prediction",
    page_icon="🏠",
    initial_sidebar_state="expanded",
)


add_logo(
    "icons8-house-96.png",
    height=70,
)

st.title("Housing Price Prediction of Indian Metro Cities")
st.subheader(
    "Use the sidebar to select the city and other features of the house to predict the price"
)

image = Image.open("house.jpg")
st.image(image, caption="Housing Price Prediction", use_column_width=True)
