import streamlit as st
import pandas as pd
import numpy as np
from helper import list_of_selected_locations_bangalore, locations_list_bangalore
from decomp import get_files
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import xgboost, lightgbm, catboost

st.set_page_config(layout="wide")


@st.cache_resource
def load_pred():
    model = get_files("Bangalore")
    return model


load_clf = load_pred()
st.title("Bangalore House Price Prediction")

st.markdown(
    """
This app predicts the **Bangalore House Price**!
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
        locations_list_bangalore,
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

    for i in list_of_selected_locations_bangalore:
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
# print("_-----------------------------------------")
# print(load_clf[3])
prediction_rf = load_clf[0].predict(df)
prediction_lgbm = load_clf[1].predict(df)
prediction_xgb = load_clf[2].predict(df)
prediction_cat = load_clf[3].predict(df)
prediction_lr = load_clf[4].predict(df)
# ["Linear Regression", "Random Forest (Best)", "XGBoost", "LGBM", "CatBoost"],
#

if model == "Linear Regression":
    curr = prediction_lr[0]
elif model == "Random Forest (Best)":
    curr = prediction_rf[0]
elif model == "XGBoost":
    curr = prediction_xgb[0]
elif model == "LGBM":
    curr = prediction_lgbm[0]
elif model == "CatBoost":
    curr = prediction_cat[0]
else:
    curr = prediction_rf[0]

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
            curr / 100000
        ),
        unsafe_allow_html=True,
    )

    meme_flag = False

    if st.checkbox("Show me the meme"):
        meme_flag = True
    if meme_flag:
        st.header("Meme Review")
        if curr <= 5000000:
            st.image("pages/img/1.png", width=350)
        elif 5000000 < curr <= 10000000:
            st.image("pages/img/2.jpg", width=350)
        elif 10000000 < curr <= 15000000:
            st.image("pages/img/3.png", width=350)
        else:
            st.image("pages/img/4.png", width=350)

stats = pd.read_csv("pages/files/test_time_accuracy_Bangalore.csv")

# create dictionary for model performance
model_performance = {
    "Linear Regression": prediction_lr[0],
    "Random Forest": prediction_rf[0],
    "XGBoost": prediction_xgb[0],
    "LGBM": prediction_lgbm[0],
    "CatBoost": prediction_cat[0],
}
with col2:
    st.line_chart(model_performance,height=350, color="#803EF5")

    st.subheader("Test time accuracy for 5 different models")
    st.line_chart(stats, height=350, x="Model", y="Accuracy", color="#803EF5")


# col1.subheader("Prediction")
# col1.write(
#     """
#     **₹ {:.2f} Lakhs**.
#     """.format(
#         prediction[0] / 100000
#     )
# )


# col2.image("https://media.giphy.com/media/3o7aDcz6Y0fzWYvU5G/giphy.gif")
