import pymysql
import time
from datetime import date

db = pymysql.connect(
    host='okus.cz8dcgq2qxno.us-east-1.rds.amazonaws.com',
    user='pitech_master',
    password='HiKrKiNpOyS5ynHiKr',
    db='productionDummy')

message_to_alert = """'Esta version de prueba vence en:

<color=#F05B60><b><size=30>{0} día{1}</size></b></color>

<size=14><color=#808080>Para adquirir su licencia contáctanos a info@okus.com.do</color></size>'
"""
cursor = db.cursor()

actual_date = date.today()
last_date = date(2019,11,26)

date_diff = last_date - actual_date

remaining_days = date_diff.days

s = 's' if remaining_days > 1 else ''

new_message = message_to_alert.format(remaining_days, s)
new_duration = 10 + ((17-remaining_days) * 2)

print(new_message)

cursor.execute('CALL update_login_alert_message_for_unlicensed_users({0},{1})'.format(new_message,new_duration))

db.commit()
