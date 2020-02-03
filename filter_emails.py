import pymysql
from random import randint

db = pymysql.connect(
    'okus.cz8dcgq2qxno.us-east-1.rds.amazonaws.com',
    'pitech_master',
    'gyJhixDogqyc3wetra6xC1Ka')
cursor = db.cursor()

UPDATE_LICENSE_STUDENTS = """
UPDATE productionDummy.students S 
	SET has_license = 0
WHERE email in ({0})
"""

SELECT_STUDENTS_EMAIL_BY_SCHOOL_GRADE_SECTION_ID = """
SELECT email
FROM productionDummy.students S
WHERE school_grade_section_id in ({0}) and has_license = 0
"""


CAFAM_sections = [
    '480',
    '481',
    '483',
    '486',
    '484',
    '487',
    '488',
    '485',
    '489',
    '490',
    '497',
    '498',	
    '505',    
    '499',
    '500',
    '501',
    '503'
]


all_emails = []
licensed_emails = []


# with open('all_emails.txt','r+') as file:
#     for line in file.readlines():
#         line_trim = line.replace('\n','')
#         all_emails.append(line_trim)

cursor.execute(
    SELECT_STUDENTS_EMAIL_BY_SCHOOL_GRADE_SECTION_ID.format(
        ','.join(CAFAM_sections)
    )
)

students_emails_from_query = cursor.fetchall()

for row_email in students_emails_from_query:
    all_emails.append(row_email[0])


# with open('licenced.txt','r+') as file:
#     for line in file.readlines():
#         line_trim = line.replace('\n','')
#         licensed_emails.append(line_trim)

# unlicenced_emails = []
# for email in all_emails:
#     if email not in licensed_emails:
#         unlicenced_emails.append(email)

# print(str(len(unlicenced_emails)))
        
# print(unlicenced_emails)

# query_to_execute = UPDATE_LICENSE_STUDENTS.format(
#     "'"+"','".join(unlicenced_emails)+"'"
# )

# print(query_to_execute)

# cursor.execute(query_to_execute)

# db.commit()


# print(str(len(all_emails)))
        
# print(all_emails)


random_emails = [all_emails[randint(0,len(all_emails))] for i in range(3)]

print (random_emails)