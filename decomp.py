import requests
import pickle
import bz2file as bz2
import gdown
import os
import joblib

drive_folder_link = "https://drive.google.com/drive/folders/15Ie_N9AwON_ArFGymBqbUdB64YipGmQL?usp=sharing"


def decompress_pickle(file):
    # print("Decompressing Files")
    # print(file)
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
