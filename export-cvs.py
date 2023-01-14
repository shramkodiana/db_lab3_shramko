import psycopg2
import csv

username = 'shramko'
database = 'lab2'
host = 'localhost'
password = '111'
port = '5432'

OUTPUT_FILE = 'db_lab3.csv'

TABLES = [
    'dinosaur',
    'species',
    'type',
    'diet'
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE.format(table), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])