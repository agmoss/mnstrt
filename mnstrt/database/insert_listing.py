"""Add a rental listing to the database"""

import datetime
import psycopg2
from . import config


def insert_listing(listing):
    """ insert a rental listing into the rental_data table """
    sql = """INSERT INTO rental_data(latitude,longitude,address,price,bedrooms,baths,type,city,company,location,utilities_included,website,intro,retrieval_date)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"""
    conn = None
    i_d = None
    try:
        params = config.config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(
            sql,
            (
                listing["latitude"],
                listing["longitude"],
                listing["address"],
                listing["price"],
                listing["bedrooms"],
                listing["baths"],
                listing["type"],
                listing["city"],
                listing["company"],
                listing["location"],
                listing["utilities_included"],
                listing["website"],
                listing["intro"],
                datetime.datetime.now(),
            ),
        )
        i_d = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return i_d
