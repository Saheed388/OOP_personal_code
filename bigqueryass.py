#UPLOAD A TABLE

from google.cloud import bigquery

import pandas_gbq
import pandas
import os


credential_path = r'C:\Users\HP\Documents\Alt_school\venv\plated-entry-385012-df33e4b65a90.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

client = bigquery.Client()
tanble_id = 'plated-entry-385012.garden.garden_sensors'

rows_to_insert =[
    {u'sensor_name': 'garden_001', u'temperatur': 88.2, u'humudity': 23.8},
    {u'sensor_name': 'garden_002', u'temperatur': 38.2, u'humudity': 53.8},
    {u'sensor_name': 'garden_002', u'temperatur': 84.2, u'humudity': 83.8},
    {u'sensor_name': 'garden_002', u'temperatur': 38.2, u'humudity': 59.8}

]

error = client.insert_rows_json(tanble_id, rows_to_insert)
if error == []:
    print("new rows as been added")
else:
    print(f'encounting error while inserting: {error}')


## TO QUERY DATA

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'alt-school-project-386517-fcb14f08a9df.json'

sql = """
SELECT *
 FROM `alt-school-project-386517.alt_school_data.titanic`
 LIMIT 10
"""

df = pandas_gbq.read_gbq(sql)
print(df)
