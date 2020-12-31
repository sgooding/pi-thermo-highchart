#!/usr/bin/python

import sys
import getopt
import sqlite3
import pandas as pd
from pathlib import Path


def process(csv_name=None, db_name=None, table_name=None):
    if csv_name is None:
        csv_name = 'temperature.csv'
    if db_name is None:
        db_name = 'temperature.db'
    if table_name is None:
        table_name = 'bailey'

    print(f'Loading csv file: {csv_name}')
    data = pd.read_csv(csv_name, names=['time', 'temperature', 'humidity'])

    # convert the time into pandas time
    print('Convert seconds into pd datetime')
    data['time'] = pd.to_datetime(data['time'], unit='s')

    print(f'Create a new database: {db_name}')
    Path(db_name).touch()

    print(f'Connecting to database: {db_name}')
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # generate the table with the date time schema
    print(f'Create a new table named: {table_name}')
    c.execute(
        f'''CREATE TABLE {table_name} (time TEXT, temperature float, humidity float)''')

    # write the data into sql
    print('Writing data to database')
    data.to_sql(table_name, conn, if_exists='append', index=False)

    c.close()

    print('Complete.')


def main(argv):
    inputfile = None
    outputfile = None
    try:
       opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
       print('convert_csv_to_sql.py -i <input.csv> -o <output.csv>')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print('convert_csv_to_sql.py -i  <input.csv> -o <output.csv>')
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg
    
    process(csv_name = inputfile, db_name = outputfile, table_name = None)

if __name__ == "__main__":
   main(sys.argv[1:])
