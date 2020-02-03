import pymysql

invivienda_student_emails = [
    '120021',
    '120066',
    '120082',
    '120204',
    '120227',
    '120269',
    '120285',
    '120374',
    '120389',
    '120422',
    '120433',
    '130513',
    '150592',
    '160655',
    '160664',
    '160686',
    '170719',
    '170726',
    '170789',
    '180011',
    '180023',
    '180032',
    '180046',
    '190075',
    '190089',
    '190093',
    '190095',
    '190121',
    '160709',
    '160695',
    '120059',
    '120076',
    '120111',
    '120232',
    '120268',
    '130449',
    '140566',
    '150585',
    '150608',
    '160701',
    '160714',
    '170735',
    '170776',
    '180006',
    '180013',
    '190101',
    '190112',
    '190117',
    '150639',
    '170765',
    '120143',
    '160651',
    '170751',
    '170755',
    '170769',
    '180016',
    '180022',
    '180036',
    '180050',
    '180081',
    '170748',
    '180054',
    '121977',
    '130459',
    '130480',
    '160646',
    '160676',
    '160702',
    '170760',
    '170762',
    '170770',
    '180029',
    '190073',
    '190076',
    '190078',
    '190086',
    '190096',
    '190099',
    '190107',
    '120102',
    '120275',
    '120408',
    '130451',
    '130511',
    '140564',
    '150598',
    '150600',
    '150617',
    '150623',
    '160650',
    '170731',
    '170771',
    '170784',
    '180012',
    '190067',
    '190085',
    '190090',
    '190100',
    '190105',
    '180055',
    '190127',
    '120161',
    '120017',
    '120055',
    '120091',
    '120274',
    '130461',
    '130500',
    '130515',
    '140560',
    '150621',
    '160660',
    '160681',
    '170782',
    '180063',
    '190113',
    '160687',
    '121940'
]

db = pymysql.connect(
    host='okus.cz8dcgq2qxno.us-east-1.rds.amazonaws.com',
    user='pitech_master',
    password='gyJhixDogqyc3wetra6xC1Ka',
    db='productionDummy')
cursor = db.cursor()

message = 'Ya es momento de que tus padres creen su cuenta de Okus. Recuerdales que tienen que completar el siguiente formulario:'

INSERT_MESSAGES_FOR_INVIVIENDA = """
INSERT INTO alert_messages (message,title,on_login,button_link,buttonText,duration,bodyFontSize,titleFontSize,username)
VALUES('{0}','¡Hola!',1,'https://forms.gle/zAD4tMiPxLoJxg4k9','Ir al formulario',10,22,16,'{1}')
"""

UPDATE_LINKS_FOR_INVIVIENDA = """
UPDATE alert_messages
SET button_link='{0}'
WHERE username in ({1})
"""

# https://forms.gle/zAD4tMiPxLoJxg4k9

cursor.execute(
    UPDATE_LINKS_FOR_INVIVIENDA.format(
        'https://docs.google.com/forms/d/1SIMM-hHisaybvOOI06trkerR0U15zW-RomRIFxLBn_c/edit',
        ','.join(invivienda_student_emails))
)

db.commit()
# for email in invivienda_student_emails:
#     cursor.execute(INSERT_MESSAGES_FOR_INVIVIENDA.format(message,email))

#     db.commit()


# results = cursor.fetchall()


