import requests
from zipfile import ZipFile
import os

username = "rubngarcamndez"
api_key = "ca6b783f599cab92cce2b0905f0fb9ce"

dataset_name = "Car Details Dataset"

url = f"https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download&select=CAR+DETAILS+FROM+CAR+DEKHO.csv"

headers = {"Authorization":f"Bearer{api_key}"}


response = requests.get(url, headers=headers)

csv_filename = f"{dataset_name}.csv"

with open(csv_filename, "wb") as csv_file:
    csv_file.write(response.content)

#with ZipFile(zip_filename, "r") as zip_ref:
#    zip_ref.extractall("./Car Details Dataset.zip")

#os.remove(csv_filename)