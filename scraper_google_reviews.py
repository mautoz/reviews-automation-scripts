import requests
import pprint as pp
import argparse
import os
import json
import pandas as pd

def get_app_search_list_result():
    current_path = os.path.dirname(os.path.realpath(__file__))
    results_list = f'{current_path}/app_search_results.csv'
    return pd.read_csv(results_list, sep=';')


def get_reviews(appId):
    url = f'http://localhost:3000/api/apps/{appId}/reviews/'
    resultado = requests.get(url)
    return resultado.json()

# resposta = get_reviews('com.google.android.calendar')

# pp.pprint(resposta)

# for key in resposta['results']['data']:
#     print("---")
#     print(key['text'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser Google API Aux")

    parser.add_argument("--search", type=str, help="App que deseja buscar")

    args = parser.parse_args()

    results = get_app_search_list_result()

    # HEADER do CSV: title;appId;url
    for linha in range(len(results)):
        reviews = get_reviews(results["appId"][linha])
        for key in reviews['results']['data']:
            print("---")
            print(key['text'])