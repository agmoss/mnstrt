"""Create database table"""

import psycopg2
from . import config


def create_table():
    """ create rental data in the PostgreSQL database"""
    command = """
        CREATE TABLE rental_data_v4 (
                id SERIAL PRIMARY KEY,
                latitude DOUBLE PRECISION,
                longitude DOUBLE PRECISION,
                address VARCHAR(255),
                price DOUBLE PRECISION,
                bedrooms VARCHAR(255), 
                baths VARCHAR(255),
                city VARCHAR(255),
                type VARCHAR(255),
                location VARCHAR(255),
                utilities_included VARCHAR(255),
                retrieval_date DATE,
                title VARCHAR(255),
                userid VARCHAR(255),
                sq_feet DOUBLE PRECISION,
                community VARCHAR(255),
                garage_size VARCHAR(255)
        )
        """
    conn = None
    try:
        params = config.config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
        print("rental_data_v4 table created")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    create_table()
