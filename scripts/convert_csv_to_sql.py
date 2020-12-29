import sqlite3
import pandas as pd
from pathlib import Path

csv_name = 'temperature.csv'
db_name = 'temperature.db'
table_name = 'bailey'

print(f'Loading csv file: {csv_name}')
data = pd.read_csv(csv_name,names=['time','temperature','humidity'])

# convert the time into pandas time
print('Convert seconds into pd datetime')
data['time'] = pd.to_datetime(data['time'],unit='s')

print(f'Create a new database: {db_name}')
Path(db_name).touch()

print(f'Connecting to database: {db_name}')
conn = sqlite3.connect(db_name)
c = conn.cursor()

# generate the table with the date time schema
print(f'Create a new table named: {table_name}')
c.execute(f'''CREATE TABLE {table_name} (time TEXT, temperature float, humidity float)''')

# write the data into sql
print('Writing data to database')
data.to_sql(table_name, conn, if_exists='append', index=False)

c.close()

print('Complete.')