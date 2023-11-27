import asyncio
from aiohttp import ClientSession
from io import StringIO
import pandas as pd
import psycopg2
import os

try:
    postgres_db = os.environ['POSTGRES_DB']
    postgres_user = os.environ['POSTGRES_USER']
    postgres_password = os.environ['POSTGRES_PASSWORD']
except Exception as e:
    print('Environment exception ', str(e))

results = []

async def get_api_data():
    async with ClientSession() as session:
        try:
            async with session.get('https://random-data-api.com/api/cannabis/random_cannabis?size=100') as response:
                try:
                    api_data = await response.json()
                    results.append(api_data)
                except Exception as e:
                    print(str(e))
        except Exception as e:
            print(str(e))

def insert_data(conn, json_batch, table):
    buffer = StringIO()
    df = pd.json_normalize(json_batch)
    df['json_data'] = df.apply(lambda x: x.to_json(), axis=1)
    col_list = str(tuple(df.columns)).replace("'", "")
    df.to_csv(buffer, header = True, index=False)
    buffer.seek(0)
    cursor = conn.cursor()
    try:
        cursor.copy_expert("COPY "+ table + col_list + " FROM STDIN WITH CSV HEADER", buffer)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
    cursor.close()

# Get big sync batches
for i in range(3):
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(10):
        # for example we have some id for http get method
        task = asyncio.ensure_future(get_api_data())
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
loop.close()

conn = psycopg2.connect(user = postgres_user, password=postgres_password, host='pg_db', port=5432, database=postgres_db)

for batch in results:
    insert_data(conn, batch, "aero.canabis_data")
conn.commit()
conn.close()

print('ok')

