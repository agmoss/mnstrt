import psycopg2
from . import config

def create_table():
    """ create rental data in the PostgreSQL database"""
    command = """
        CREATE TABLE rental_data (
                id SERIAL PRIMARY KEY,
                latitude DOUBLE PRECISION,
                longitude DOUBLE PRECISION,
                address VARCHAR(255),
                price DOUBLE PRECISION,
                bedrooms VARCHAR(255), 
                baths INTEGER,
                type VARCHAR(255),
                city VARCHAR(255),
                company VARCHAR(255),
                location VARCHAR(255),
                utilities_included BOOLEAN,
                website VARCHAR(255),
                intro VARCHAR(255),
                retrieval_date DATE
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
        print('rental_data table created')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    create_table()
