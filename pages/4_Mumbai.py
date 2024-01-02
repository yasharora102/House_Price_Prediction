import streamlit as st
import pandas as pd
import numpy as np
from helper import list_of_selected_locations_mumbai, locations_list_mumbai
from decomp import get_files


@st.cache_resource
def load_pred():
    model = get_files("Mumbai")
    return model


load_clf = load_pred()
st.title("Mumbai House Price Prediction")

st.markdown(
    """
This app predicts the **Mumbai House Price**!
"""
)
st.sidebar.header("User Input Features")


# Collects user input features into dataframe
def user_input_features():
    location = st.sidebar.selectbox(
        "Location",
        locations_list_mumbai,
        index=0,
    )
    Area = st.sidebar.slider("Area", 100, 10000, 1000)
    No_of_Bedrooms = st.sidebar.slider("No. of Bedrooms", 1, 10, 2)
    Resale = st.sidebar.slider("Resale", 0, 1, 1)
    Gasconnection = st.sidebar.slider("Gasconnection", 0, 1, 1)
    Childrensplayarea = st.sidebar.slider("Children'splayarea", 0, 1, 1)
    LiftAvailable = st.sidebar.slider("LiftAvailable", 0, 1, 1)
    Wardrobe = st.sidebar.slider("Wardrobe", 0, 1, 1)
    Price_per_sqft = st.sidebar.slider("Price_per_sqft", 100, 10000, 1000)
    data = {
        "Area": Area,
        "No. of Bedrooms": No_of_Bedrooms,
        "Resale": Resale,
        "Gasconnection": Gasconnection,
        "Children'splayarea": Childrensplayarea,
        "LiftAvailable": LiftAvailable,
        "Wardrobe": Wardrobe,
        "Price_per_sqft": Price_per_sqft,
    }

    features = pd.DataFrame(data, index=[0])
    # crete location variable according to the selected location
    selected_location = "Location_" + location
    # features[selected_location] = 1

    for i in list_of_selected_locations_mumbai:
        if i == selected_location:
            features[i] = 1
        else:
            features[i] = 0
    # create location variable for other location

    # features = pd.DataFrame(data, index=[0])
    return features, location


df, location = user_input_features()

st.subheader("User Input parameters")

user_input = {
    "Area": df["Area"].values[0],
    "No. of Bedrooms": df["No. of Bedrooms"].values[0],
    "Resale": df["Resale"].values[0],
    "Gasconnection": df["Gasconnection"].values[0],
    "Children'splayarea": df["Children'splayarea"].values[0],
    "LiftAvailable": df["LiftAvailable"].values[0],
    "Wardrobe": df["Wardrobe"].values[0],
    "Price_per_sqft": df["Price_per_sqft"].values[0],
    "Location": location,
}

# Creating a Markdown table using st.write
st.write(
    "| Parameter | Value |"
    + "\n"
    + "| :--- | :--- |"
    + "\n"
    + "\n".join(f"| {key} | **{value}** |" for key, value in user_input.items())
)

# Apply model to make predictions
prediction = load_clf.predict(df)


st.subheader("Prediction")
st.write(
    """
    The predicted price of the house is **₹ {:.2f} Lakhs**.
    """.format(
        prediction[0] / 100000
    )
)
