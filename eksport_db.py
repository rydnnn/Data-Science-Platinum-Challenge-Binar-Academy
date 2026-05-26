import sqlite3
import pandas as pd

df = pd.read_csv('finish-data-set.csv')

df.columns = df.columns.str.strip()

connection = sqlite3.connect('binar.db')

df.to_sql('cleansing_data', connection, if_exists='replace')

# note ; gunakan "SQLITE VIEWER" untuk melihat database