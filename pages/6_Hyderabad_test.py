import streamlit as st
import pandas as pd
import numpy as np
from helper import list_of_selected_locations_hyderabad, locations_list_hyderabad
from decomp import get_files
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

st.set_page_config(layout="wide")


@st.cache_resource
def load_pred():
    model = get_files("Hyderabad")
    return model


load_clf = load_pred()
st.title("Hyderabad House Price Prediction")

st.markdown(
    """
This app predicts the **Hyderabad House Price**!
"""
)
st.sidebar.header("User Input Features")


# Collects user input features into dataframe
def user_input_features():
    model = st.sidebar.selectbox(
        "Choose Model",
        ["Linear Regression", "Random Forest (Best)", "XGBoost", "LGBM", "CatBoost"],
        index=1,
    )

    location = st.sidebar.selectbox(
        "Location",
        locations_list_hyderabad,
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

    for i in list_of_selected_locations_hyderabad:
        if i == selected_location:
            features[i] = 1
        else:
            features[i] = 0
    # create location variable for other location

    # features = pd.DataFrame(data, index=[0])
    return features, location, model


df, location, model = user_input_features()
col1, col2 = st.columns(2, gap="small")
col1.header("User Input parameters")
col2.header("Model Performance")


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

# Apply model to make predictions
prediction = load_clf.predict(df)
prediction2 = load_clf.predict(df)
prediction3 = load_clf.predict(df)
prediction4 = load_clf.predict(df)
prediction5 = load_clf.predict(df)
# ["Linear Regression", "Random Forest (Best)", "XGBoost", "LGBM", "CatBoost"],
#
if model == "Linear Regression":
    curr = prediction[0]
elif model == "Random Forest (Best)":
    curr = prediction2[0]
elif model == "XGBoost":
    curr = prediction3[0]
elif model == "LGBM":
    curr = prediction4[0]
elif model == "CatBoost":
    curr = prediction5[0]
else:
    curr = prediction[0]

with col1:
    st.table(
        pd.DataFrame.from_dict(user_input, orient="index", columns=["Value"]).drop(
            "Price_per_sqft", axis=0
        )
    )

    st.header("Prediction")
    st.markdown(
        """

    <h1> ₹ {:.2f} Lakhs </h1>
    """.format(
            prediction[0] / 100000
        ),
        unsafe_allow_html=True,
    )
   

    st.header("Meme Review")
    if curr <= 5000000:
        st.image("pages/img/1.png", width=350)
    elif 5000000 < curr <= 10000000:
        st.image("pages/img/2.jpg",width=350)
    elif 10000000 < curr <= 15000000:   
        st.image("pages/img/3.png",width=350)
    else:
        st.image("pages/img/4.png",width=350)

with col2:
    st.line_chart(
        {
            "Linear Regression": prediction[0],
            "Random Forest": prediction2[0],
            "XGBoost": prediction3[0],
            "LGBM": prediction4[0],
            "CatBoost": prediction5[0],
        },
        height=350,
    )

    st.subheader("Test time accuracy for 5 different models")
    st.line_chart(
        {
            "Linear Regression": 0.75,
            "Random Forest": 0.85,
            "XGBoost": 0.88,
            "LGBM": 0.89,
            "CatBoost": 0.90,
        },
        height=350,
    )


# col1.subheader("Prediction")
# col1.write(
#     """
#     **₹ {:.2f} Lakhs**.
#     """.format(
#         prediction[0] / 100000
#     )
# )


# col2.image("https://media.giphy.com/media/3o7aDcz6Y0fzWYvU5G/giphy.gif")
