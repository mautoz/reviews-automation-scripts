import json
from os.path import join
import requests
import pprint as pp
import os
import argparse


# Retorna a lista com a busca por nome de um App
def get_reviews(appName):
    url = f'http://localhost:3000/api/apps/?q={appName}'
    result = requests.get(url)
    return result.json()


# Insere as opções no .csv
def get_list_of_apps(appName):
    response = get_reviews(appName)

    results = []
    current_path = os.path.dirname(os.path.realpath(__file__))
    results_list = f'{current_path}/app_search_results.csv'
    with open(results_list, "a", encoding='utf-8') as file:
        #file.write('title;appId\n')
        for app in response['results']:
            file.write(f'{app["title"]};{app["appId"]}\n')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser Google API Aux")
    parser.add_argument("--search", type=str, help="App que deseja buscar")
    args = parser.parse_args()

    # Faz uma busca com o termo passado e salva o resultado em "app_search_results.txt"
    get_list_of_apps(args)
    
