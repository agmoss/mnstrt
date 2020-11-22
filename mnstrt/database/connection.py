"""Provide a connection object to functions that need to access the database"""

import psycopg2
from . import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        params = config.config()

        print("Connecting to the PostgreSQL database...")

        conn = psycopg2.connect(**params)

        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    connect()
