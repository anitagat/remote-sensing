# Import modules
import copernicus_marine_client as copernicus_marine
import xarray as xr 
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

username = ""
password = ""

# Load client credentials from a JSON file
with open('config.json','r') as config_file:
    config = json.load(config_file)
    username = config["CopernicusMarine"]['username']
    password = config["CopernicusMarine"]['password']

print("Config file read")

# Load dataframe
request_dataframe = copernicus_marine.read_dataframe(
    dataset_id = "cmems_mod_med_wav_myint_4.2km_PT1H-i",
    username=username,
    password=password,
    minimum_longitude = 7.3127958575960506,                         # West Italy
    maximum_longitude = 18.99235157323233,                          # East Italy
    minimum_latitude = 36.51998113712651,                           # South Italy
    maximum_latitude = 45.43607054504527,                           # North Italy 
    variables = ["VHM0", "VHM0_SW1", "VHM0_SW2", "VHM0_WW"],
    start_datetime = "2021-01-01T00:00:00",
    end_datetime = "2021-02-28T23:00:00"
)

# Print loaded dataset information
print(request_dataframe)

# drop NAs
request_dataframe = request_dataframe.dropna()

# to CSV
wave_df_csv = request_dataframe.to_csv("wave-data-2021.csv")

### Descriptive stats ##
# Rename file for ease
wave_df = request_dataframe
print(wave_df.describe())
