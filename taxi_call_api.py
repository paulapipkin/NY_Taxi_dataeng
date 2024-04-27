# Load the packages
import json
import requests
import pandas as pd


def calls_taxi_api_data(url, headers, data_filter_number):
    response = requests.get(url, headers=headers).json()
    data_subset = response[:data_filter_number]
    return data_subset


def write_csv():
    # Load the credentials from the JSON file
    with open('Desktop/DataProjTaxi/credentials.json') as json_file:
        credentials = json.load(json_file)

    # Extract the username and password from the loaded JSON data
    username = credentials.get('username')
    password = credentials.get('password')
    data = calls_taxi_api_data(
        'https://data.cityofnewyork.us/resource/biws-g3hs.json',
        {'X-ApiKeys': 'accessKey=' + username + '; secretKey=' + password}, 2000)
    sub_df = pd.DataFrame(data)
    sub_df.to_csv("Desktop/DataProjTaxi/first_2000_rows.csv", index=False)


write_csv()
