import pandas as pd

from ..database import connection

def data_for_analysis():
    df = pd.read_sql(
        "SELECT * FROM rental_data",
        connection.connect(),
    )

    print('Data description')
    print(df.describe())
    return df
