import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

dataset_name = "Car Details Dataset"

api.dataset_download_files(dataset_name, path='./', force=False, quiet=True, unzip=True)

