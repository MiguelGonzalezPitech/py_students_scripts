import pymysql
import json
db = pymysql.connect(
    host='okus.cz8dcgq2qxno.us-east-1.rds.amazonaws.com',
    user='pitech_master',
    password='HiKrKiNpOyS5ynHiKr',
    db='productionDummy')
cursor = db.cursor()

GET_BLOCKS_THAT_ARE_NOT_IN_STAGING = """
SELECT *
FROM productionDummy.blocks
WHERE id NOT IN (select id from staging.blocks)
"""

cursor.execute(GET_BLOCKS_THAT_ARE_NOT_IN_STAGING)

blocks = cursor.fetchall()

new_blocks = []

for row in blocks:
    new_blocks.append({
        'long_id': row[0],
        'name': row[1],
        'max_quantity': row[2],
        'retry': row[3]
    })
print(new_blocks)

with open('blocks.json', 'w') as json_file:
  json.dump(new_blocks, json_file)