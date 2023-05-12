from google.cloud import bigquery
import os
import pandas_gbq
import pandas



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'alt-school-project-386517-fcb14f08a9df.json'
client = bigquery.Client()

sql_code = """
SELECT *
 FROM `alt-school-project-386517.alt_school_data.titanic`
LIMIT 20
"""
#CAN ALSO BE USE
# query_work = client.query(sql_code)

# for row in query_work.result():
#     print(row)

df = pandas_gbq.read_gbq(sql_code)
print(df)
