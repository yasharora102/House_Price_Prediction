import streamlit as st
from PIL import Image
from decomp import download_files, get_files
import os

# check if all files present in the compressed folder else download them

if not os.path.exists("compressed/bangalore_house_price_model.pkl.pbz2"):
    with st.spinner("Downloading files from Google Drive Folder"):
        download_files()
else:
    pass

# @st.cache_resource
# def get_model(name):
#     if name == "Bangalore":
#         return bangalore_house_price_model
#     elif name == "Hyderabad":
#         return hyderabad_house_price_model
#     elif name == "Kolkata":
#         return kolkata_house_price_model
#     elif name == "Mumbai":
#         return mumbai_house_price_model
#     elif name == "Delhi":
#         return delhi_house_price_model
#     else:
#         return None
st.title("Housing Price Prediction of Indian Metro Cities")
st.subheader(
    "Use the sidebar to select the city and other features of the house to predict the price"
)

image = Image.open("house.jpg")
st.image(image, caption="Housing Price Prediction", use_column_width=True)


