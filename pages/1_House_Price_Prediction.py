import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
from streamlit_extras.app_logo import add_logo

warnings.filterwarnings("ignore")
from decomp import decompress_pickle
import os


st.set_page_config(
    layout="wide",
    page_title="House Price Prediction",
    page_icon="🏠",
    initial_sidebar_state="expanded",
)

model_dir = "models"
add_logo(
    "icons8-house-96.png",
    height=70,
)


@st.cache_resource
def load_models():
    rf_regressor = pickle.load(
        open(os.path.join(model_dir, "RandomForestRegressor.pkl"), "rb")
    )
    lr_regressor = pickle.load(
        open(os.path.join(model_dir, "LinearRegression.pkl"), "rb")
    )
    dt_regressor = pickle.load(
        open(os.path.join(model_dir, "DecisionTreeRegressor.pkl"), "rb")
    )
    xgb_regressor = pickle.load(open(os.path.join(model_dir, "XGBRegressor.pkl"), "rb"))
    lgb_regressor = pickle.load(
        open(os.path.join(model_dir, "LGBMRegressor.pkl"), "rb")
    )
    cb_regressor = pickle.load(
        open(os.path.join(model_dir, "CatBoostRegressor.pkl"), "rb")
    )
    X = pd.read_csv("pages/files/X.csv")
    Data = pd.read_csv("pages/files/Original.csv")

    return (
        rf_regressor,
        lr_regressor,
        dt_regressor,
        xgb_regressor,
        lgb_regressor,
        cb_regressor,
        X,
        Data,
    )


(
    rf_regressor,
    lr_regressor,
    dt_regressor,
    xgb_regressor,
    lgb_regressor,
    cb_regressor,
    X,
    Original,
) = load_models()


# adsiuiausduyhgadhsujigvhj
def model_prediction(city, area, sqft, bhk, park, ac, wifi, lift, security):
    city_index = np.where(X.columns == city)[0][0]
    area_index = np.where(X.columns == area)[0][0]
    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = park
    x[3] = ac
    x[4] = wifi
    x[5] = lift
    x[6] = security
    if city_index >= 0:
        x[city_index] = 1
    if area_index >= 0:
        x[area_index] = 1
    return (
        rf_regressor.predict([x])[0],
        lr_regressor.predict([x])[0],
        dt_regressor.predict([x])[0],
        xgb_regressor.predict([x])[0],
        lgb_regressor.predict([x])[0],
        cb_regressor.predict([x])[0],
    )


st.title("Indian Metropolitan House Price Prediction")

st.sidebar.header("User Input Features")

# Load data
df = pd.read_csv("pages/files/X.csv")


# Collects user input features into dataframe
def user_input_features(df=df, Original=Original):
    model = st.sidebar.selectbox(
        "Choose Model",
        [
            "Linear Regression",
            "Random Forest (Best)",
            "XGBoost",
            "LGBM",
            "CatBoost",
            "DecisionTreeRegressor",
        ],
        index=1,
    )

    city = st.sidebar.selectbox(
        "Choose City",
        ["Banglore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"],
        index=0,
    )

    original_dataset = Original[Original["City"] == city]

    all_locations = original_dataset["Area"].unique()
    all_locations.sort()

    required_locations = list(df.columns[7:])
    required_locations.sort()

    filtered_locations = list(set(all_locations) & set(required_locations))
    filtered_locations.sort()

    filtered_locations.sort()
    location = st.sidebar.selectbox(
        "Location",
        filtered_locations,
        index=0,
    )

    sqft = st.sidebar.slider("Sqft", 100, 10000, 1000)
    bhk = st.sidebar.slider("BHK", 1, 10, 2)

    park = st.sidebar.slider("Park", 0, 1, 1)
    ac = st.sidebar.slider("AC", 0, 1, 1)
    wifi = st.sidebar.slider("Wifi", 0, 1, 1)
    lift = st.sidebar.slider("Lift", 0, 1, 1)
    security = st.sidebar.slider("Security", 0, 1, 1)

    data = {
        "City": city,
        "Location": location,
        "Area": sqft,
        "BHK": bhk,
        "Park": park,
        "AC": ac,
        "Wifi": wifi,
        "Lift": lift,
        "Security": security,
    }

    return data, model


data, model = user_input_features()
col1, col2 = st.columns(2, gap="small")
col1.header("User Input parameters")
col2.header("Model Performance")


preds = model_prediction(
    data["City"],
    data["Location"],
    data["Area"],
    data["BHK"],
    data["Park"],
    data["AC"],
    data["Wifi"],
    data["Lift"],
    data["Security"],
)

if model == "Linear Regression":
    curr = preds[1]
elif model == "Random Forest (Best)":
    curr = preds[0]
elif model == "XGBoost":
    curr = preds[3]
elif model == "LGBM":
    curr = preds[4]
elif model == "CatBoost":
    curr = preds[5]
elif model == "DecisionTreeRegressor":
    curr = preds[2]
else:
    curr = preds[0]


with col1:
    st.table(
        pd.DataFrame.from_dict(data, orient="index").rename(
            columns={0: "Input Parameters"}
        )
    )

    st.header("Prediction")
    st.markdown(
        """

    <h1> ₹ {:.2f} Lakhs </h1>
    """.format(
            curr
        ),
        unsafe_allow_html=True,
    )

    meme_flag = False

    if st.checkbox("Show me the meme"):
        meme_flag = True

        if meme_flag and curr <= 75:
            st.image("pages/img/1.png", width=300)
        elif meme_flag and (curr > 75 and curr <= 100):
            st.image("pages/img/2.jpg", width=300)
        elif meme_flag and (curr > 100 and curr <= 150):
            st.image("pages/img/3.png", width=300)
        else:
            st.image("pages/img/4.png", width=300)


stats = pd.read_csv("pages/files/all.csv")

# create dictionary for model performance
model_performance = {
    "Linear Regression": preds[1],
    "Random Forest (Best)": preds[0],
    "XGBoost": preds[3],
    "LGBM": preds[4],
    "CatBoost": preds[5],
    "DecisionTreeRegressor": preds[2],
}
with col2:
    st.line_chart(model_performance, height=350, color="#803EF5")

    st.subheader("Test time accuracy for 5 different models")
    st.line_chart(stats, height=350, x="Model", y="Accuracy", color="#803EF5")
