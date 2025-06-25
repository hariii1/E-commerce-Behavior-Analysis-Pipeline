import psycopg2
import pandas as pd
from tabulate import tabulate  

def data():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="admin@321",
        dbname="DataENG"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM e_commerce")

    columns = [desc[0] for desc in cursor.description]

    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=columns)

    print(tabulate(df))

    cursor.close()
    conn.close()

    return df

df = data()

