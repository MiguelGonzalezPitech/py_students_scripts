import pymysql

db = pymysql.connect(
    host='okus.cz8dcgq2qxno.us-east-1.rds.amazonaws.com',
    user='pitech_master',
    password='gyJhixDogqyc3wetra6xC1Ka',
    db='productionDummy')
cursor = db.cursor()




MONTESSORI_sections = [
    '568',
    '569',
    '570',
    '571',
    '572',
    '573'
]


# with open('all_emails.txt','r+') as file:
#     for line in file.readlines():
#         line_trim = line.replace('\n','')
#         all_emails.append(line_trim)


SELECT_STUDENTS_EMAIL_BY_SCHOOL_GRADE_SECTION_ID = """
SELECT email
FROM productionDummy.students S
WHERE school_grade_section_id in ({0})
"""

all_emails = []

cursor.execute(
    SELECT_STUDENTS_EMAIL_BY_SCHOOL_GRADE_SECTION_ID.format(
        ','.join(MONTESSORI_sections)
    )
)

students_emails_from_query = cursor.fetchall()

for row_email in students_emails_from_query:
    all_emails.append(row_email[0])

INSERT_MESSAGES_FOR_MONTESSORI = """
INSERT INTO alert_messages (message,title,on_login,button_link,buttonText,duration,bodyFontSize,titleFontSize,username)
VALUES('{0}','¡Hola!',1,'https://docs.google.com/forms/d/1HPGcAQ_3-j5aH6m_0TsV4O05mDxkDZivTc61Ud8ww9g/edit','Ir al formulario',10,22,16,'{1}')
"""
message = 'Ya es momento de que tus padres creen su cuenta de Okus. Recuerdales que tienen que completar el siguiente formulario:'

# https://forms.gle/zAD4tMiPxLoJxg4k9

for i in all_emails:
    cursor.execute(
        INSERT_MESSAGES_FOR_MONTESSORI.format(
            message,
            i)
    )

    db.commit()
