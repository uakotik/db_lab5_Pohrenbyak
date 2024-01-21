import csv
import decimal
import psycopg2

username = 'student01'
password = '1'
database = 'lab5'

INPUT_CSV_FILE = 'cereal.csv'

query_00 = '''
DROP TABLE IF EXISTS cereal_new
'''

query_0 = '''
CREATE TABLE cereal_new
(
  name VARCHAR(100) NOT NULL,
  type VARCHAR(3) NOT NULL,
  calories INT NOT NULL,
  cereal_id INT NOT NULL,
  protein INT NOT NULL,
  fat INT NOT NULL,
  sugar INT NOT NULL,
  manufacturer_id VARCHAR(3) NOT NULL,
  PRIMARY KEY (cereal_id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(manufacturer_id)
);
'''

query_1 = '''
DELETE FROM cereal_new
'''

query_2 = '''
INSERT INTO cereal_new (name, type, calories, cereal_id,protein,fat,sugar,manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_00)
    cur.execute(query_0)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            print(idx)
            values = (row['name'], row['type'], row['calories'],idx+1,row['protein'],row['fat'],row['sugars'],row['mfr']) 
            cur.execute(query_2, values)

    conn.commit()
