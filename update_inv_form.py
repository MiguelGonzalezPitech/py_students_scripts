import pymysql
import time
from datetime import date

inv_emails = [
'120285',
'120374',
'130513',
'160686',
'180023',
'190075',
'190121',
'160709',
'120059',
'120076',
'120111',
'130449',
'140566',
'150585',
'150608',
'160701',
'160714',
'180006',
'190101',
'190117',
'160651',
'170755',
'170769',
'180036',
'180050',
'121977',
'130459',
'130480',
'160646',
'160676',
'160702',
'170760',
'190099',
'190107',
'120275',
'130511',
'140564',
'150617',
'150623',
'160650',
'170731',
'190067',
'190090',
'190100',
'120055',
'120091',
'120274',
'130461',
'130500',
'130515',
'160660',
'160681',
'170782',
'190113'
]

db = pymysql.connect(
    host='okus.cz8dcgq2qxno.us-east-1.rds.amazonaws.com',
    user='pitech_master',
    password='gyJhixDogqyc3wetra6xC1Ka',
    db='productionDummy')
cursor = db.cursor()

update_students = """
UPDATE alert_messages
SET on_login = 0, sent=1
WHERE username in ({0})
"""
print()
cursor.execute(
    update_students.format(
        ','.join(inv_emails)
    )
)
db.commit()