import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(
            database="mnstrt",
            user="mnstrtuser",
            password="mnstrtpass",
            host="127.0.0.1",
            port="5432",
        )

        cur = conn.cursor()

        print("PostgreSQL database version:")
        cur.execute("SELECT version()")

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")
