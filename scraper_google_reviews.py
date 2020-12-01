import requests
import os
from datetime import datetime
import pandas as pd

from helpers import db_aux


def get_app_search_list_result():
    current_path = os.path.dirname(os.path.realpath(__file__))
    results_list = f'{current_path}/app_search_results.csv'
    return pd.read_csv(results_list, header=None, sep=';')


def get_reviews(appId):
    url = f'http://localhost:3000/api/apps/{appId}/reviews/'
    resultado = requests.get(url)
    return resultado.json()


def insert_reviews_db(conn, results):
    # HEADER do CSV: title;appId (0, 1)
    for line in range(len(results)):
        reviews = get_reviews(results[1][line])
        for key in reviews['results']['data']:
            date_db = datetime.strptime(key['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            if db_aux.search_row(conn, date_db) is None:
                review_new = {}
                review_new["scraper_date"] = datetime.strptime(key['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
                review_new["source"] = "Google"
                review_new["app_name"] = results[0][line]
                review_new["language"] = "en"
                review_new["review_content"] = key['text']
                db_aux.insert_db(conn, review_new)


if __name__ == "__main__":

    db_credentials = {
        'host' : os.getenv('POSTGRES_HOST'),
        'dbname' : os.getenv('POSTGRES_DATABASE'),
        'user' : os.getenv('POSTGRES_USER'),
        'password' : os.getenv('POSTGRES_PASSWORD'),
        'port' : os.getenv('POSTGRES_PORT') 
    }

    results = get_app_search_list_result()

    with db_aux.connect_db(db_credentials) as conn:
        insert_reviews_db(conn, results)
