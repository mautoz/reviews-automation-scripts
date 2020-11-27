import psycopg2 as db
from random import randrange
import random as rand
import datetime
import unidecode
from contextlib import contextmanager


rand.seed(datetime.datetime.now())


@contextmanager
def connect_db(db_credentials):
    conn = db.connect(**db_credentials)
    print("Conectando ao BD!")
    yield conn
    conn.close()


def number_rows(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT count(*) FROM {table}")
    result = cur.fetchone()
    return result[0]
