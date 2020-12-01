import psycopg2 as db
from random import randrange
import random as rand
import datetime
import unidecode
from contextlib import contextmanager


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


def rows_human_decision(conn):
    cur = conn.cursor()
    cur.execute(f"select count(*) from reviews_data where is_a11y_human = 1 or is_a11y_human = 0")
    result = cur.fetchone()
    return result[0]


def insert_db(conn, review):
    try:
        cur = conn.cursor()
        query = f"INSERT INTO reviews_data ( \
                scraper_date, \
                review_source, \
                review_app, \
                review_language, \
                review_raw \
            ) VALUES (%s, %s, %s, %s, %s)"
        values = (
            review["scraper_date"],
            review["source"],
            review["app_name"],
            review["language"],
            review["review_content"]
        )
        cur.execute(query, values)
        print("+ Inserting...")
        conn.commit()
    except Exception as err:
        print(err)
        print("- Something get wrong! The file wasn't inserted!")
        raise


def search_row(conn, date_db):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM reviews_data WHERE scraper_date='{date_db}'")
    return cur.fetchone()