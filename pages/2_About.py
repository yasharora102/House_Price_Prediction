import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    layout="wide", page_title="About", page_icon="ℹ️", initial_sidebar_state="collapsed"
)


# Hide sidebar
add_logo(
    "icons8-house-96.png",
    height=70,
)


def about_page():
    st.title("About")

    col1, col2 = st.columns(2, gap="large")

    # Left column with group image
    with col1:
        st.markdown(
            """
        <h3>Group Members:</h3>
        """,
            unsafe_allow_html=True,
        )
        st.image("group.jpg", use_column_width=True)

    # Right column with project information
    with col2:
        st.markdown(
            """
        This project aims to predict house prices using machine learning techniques.
        
        **Dataset**: The dataset used for training the models was obtained from [Kaggle](https://www.kaggle.com/datasets/sonukiller99/indian-house-price-combined).
        
        **Models**: We have used various machine learning models such as: 
        - Linear Regression
        - Decision Tree Regressor
        - Random Forest Regressor
        - XGBoost
        - LightGBM
        - CatBoost
        
        **Research Paper**: You can find the research paper related to this project [here](https://drive.google.com/file/d/1erSeT8rseePqqyXmOC0EhtBZt39SJgmH/view?usp=sharing).
        
        Made with ❤️ by:
        - [Yash Arora](https://yasharora102.github.io)
        - [Deepti Ranjan Das]()
        - [Sreeram S Nair]()
        - [Nanhe Singh]()
        - [Yash Bhardwaj]()
    """
        )


about_page()
