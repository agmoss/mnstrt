import psycopg2


def create_table():
    """ create rental data in the PostgreSQL database"""
    command = """
        CREATE TABLE rental_data (
                id SERIAL PRIMARY KEY,
                latitude DOUBLE PRECISION,
                longitude DOUBLE PRECISION,
                address VARCHAR(255),
                price DOUBLE PRECISION,
                bedrooms INTEGER, 
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
        conn = psycopg2.connect(
            database="mnstrt",
            user="mnstrtuser",
            password="mnstrtpass",
            host="127.0.0.1",
            port="5432",
        )
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    create_table()
