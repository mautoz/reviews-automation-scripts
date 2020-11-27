import os
import datetime

from helpers import db_aux


db_credentials = {
    'host' : os.getenv('POSTGRES_HOST'),
    'dbname' : os.getenv('POSTGRES_DATABASE'),
    'user' : os.getenv('POSTGRES_USER'),
    'password' : os.getenv('POSTGRES_PASSWORD'),
    'port' : os.getenv('POSTGRES_PORT') 
}

with db_aux.connect_db(db_credentials) as conn:
    current_path = os.path.dirname(os.path.realpath(__file__))
    scraper_log = f'{current_path}/scraper.log'
    with open(scraper_log, "a") as myfile:
        myfile.write(f'{datetime.datetime.now()}\tA tabela de reviews contém: {db_aux.number_rows(conn, "reviews_data")} linhas!\n')
    
    contato_log = f'{current_path}/contato.log'
    with open(contato_log, "a") as myfile:
        myfile.write(f'{datetime.datetime.now()}\tExistem: {db_aux.number_rows(conn, "contato")} contatos registrados!\n')

