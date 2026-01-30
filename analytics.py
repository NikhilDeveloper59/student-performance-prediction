import sqlite3
import pandas as pd



def load_data():
    conn = sqlite3.connect("students.db")
    df = pd.read_sql_query("SELECT * FROM records", conn)
    conn.close()
    return df
