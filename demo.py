# import the smtplib module. It should be included in Python by default
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
password = ''
with open(dir_path+'\pss.txt','r') as pss:
    password = pss.readline()

s.login('mrmiguetara@gmail.com', password)

msg = MIMEMultipart()       # create a message

# add in the actual person name to the message template
message = 'El chicharron no es carne'

# setup the parameters of the message
msg['From']= 'miguel.gonzalez@pitech.com.do'
msg['To']='ricardo.vasquez@pitech.com.do'
msg['Subject']="This is TEST"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)