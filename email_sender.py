import smtplib
from email.message import EmailMessage

# create a email_settings.py file with enums that contain user_id and pwd of your gmail account
# like this

# from enum import Enum

# class Email(Enum):
#     USER_ID = "some gmail account user id"
#     PASSWORD = "password for that gmail account"

from email_settings import Email 
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())

#smtplib sets up a smtp server

email = EmailMessage()
email["from"] = "Vinod Python Kumar"
email["to"] = "vkviswa@gmail.com"
email["subject"] = "Test sending email from python script"

email.set_content(html.substitute({"name": "TinTin"}), "html")
with smtplib.SMTP(host="smtp.gmail.com", port=587)  as smtp:# these values are fixed for gmail
    smtp.ehlo() #starts the server with a mis-spelt hello
    smtp.starttls() # starts encryption mechanism
    smtp.login(Email.USER_ID.value, Email.PASSWORD.value)
    smtp.send_message(email)
    smtp.close()
    print("message sent")
