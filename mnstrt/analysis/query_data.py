"""Use stored data for analysis"""

import pandas as pd

from ..database import connection


def data_for_analysis():
    """Create dataframe from database"""

    conn = None
    try:
        conn = connection.connect()
        df = pd.read_sql(
            "SELECT * FROM rental_data",
            conn,
        )

        print("Data description")
        print(df.describe())
        return df
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")
