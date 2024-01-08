import requests
import pickle
import bz2file as bz2
import gdown
import os
import joblib

drive_folder_link = "https://drive.google.com/drive/folders/15Ie_N9AwON_ArFGymBqbUdB64YipGmQL?usp=sharing"


def decompress_pickle(file):
    data = bz2.BZ2File(file, "rb")
    data = pickle.load(data)
    print(f"{file} Decompressed")
    return data

def decompress_pickle_joblib(file):
    data = bz2.BZ2File(file, "rb")
    data = joblib.load(data)
    print(f"{file} Decompressed")
    return data

def download_files():
    # Downloading files from Google Drive Folder
    print("Downloading files from Google Drive Folder")
    gdown.download_folder(drive_folder_link, quiet=False, use_cookies=False)
    print("Download Completed")


def get_files(file):

    if file == "Bangalore":
        bangalore_house_price_model_rf = decompress_pickle_joblib(
            "compressed/bangalore/bangalore_house_price_model_random_forest_model.pkl.pbz2"
        )

        bangalore_house_price_model_lgbm = decompress_pickle_joblib(
            "compressed/bangalore/bangalore_house_price_model_lgbm_model.pkl.pbz2"
        )

        # bangalore_house_price_model_xgb = decompress_pickle(
        #     "compressed/bangalore/bangalore_house_price_model_xgb_model.pkl.pbz2"
        # )
        bangalore_house_price_model_xgb = decompress_pickle_joblib(
            "compressed/bangalore/bangalore_house_price_model_xgb_model.pkl.pbz2"
        )

        bangalore_house_price_model_cat = decompress_pickle_joblib(
            "compressed/bangalore/bangalore_house_price_model_catboost_model.pkl.pbz2"
        )

        bangalore_house_price_model_lr = decompress_pickle_joblib( 
            "compressed/bangalore/bangalore_house_price_model_lr.pkl.pbz2"
        )
        return bangalore_house_price_model_rf, bangalore_house_price_model_lgbm, bangalore_house_price_model_xgb, bangalore_house_price_model_cat, bangalore_house_price_model_lr
    
    elif file == "Hyderabad":
        hyderabad_house_price_model = decompress_pickle(
            "compressed/hyderabad_house_price_model.pkl.pbz2"
        )
        return hyderabad_house_price_model
    elif file == "Kolkata":
        kolkata_house_price_model = decompress_pickle(
            "compressed/kolkata_house_price_model.pkl.pbz2"
        )
        return kolkata_house_price_model
    elif file == "Mumbai":
        mumbai_house_price_model = decompress_pickle(
            "compressed/mumbai_house_price_model.pkl.pbz2"
        )
        return mumbai_house_price_model
    elif file == "Delhi":
        delhi_house_price_model = decompress_pickle(
            "compressed/delhi_house_price_model.pkl.pbz2"
        )
        return delhi_house_price_model
    else:
        return None
    

    # bangalore_house_price_model = decompress_pickle(
    #     "compressed/bangalore_house_price_model.pkl.pbz2"
    # )
    # hyderabad_house_price_model = decompress_pickle(
    #     "compressed/hyderabad_house_price_model.pkl.pbz2"
    # )
    # kolkata_house_price_model = decompress_pickle(
    #     "compressed/kolkata_house_price_model.pkl.pbz2"
    # )
    # mumbai_house_price_model = decompress_pickle(
    #     "compressed/mumbai_house_price_model.pkl.pbz2"
    # )
    # delhi_house_price_model = decompress_pickle(
    #     "compressed/delhi_house_price_model.pkl.pbz2"
    # )

    # return (
    #     bangalore_house_price_model,
    #     hyderabad_house_price_model,
    #     kolkata_house_price_model,
    #     mumbai_house_price_model,
    #     delhi_house_price_model,
    # )
