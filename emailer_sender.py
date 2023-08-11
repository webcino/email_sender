import os
from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib

load_dotenv()

email_sender = 'alcino.namba20@gmail.com'
email_password = os.environ.get('EMAIL_PASSWORD')

email_receiver = 'havaj37708@touchend.com'

subject = 'Python Email Sender Tutorial'

body = """
This is confirmation that email was sent and tutorial has worked!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtplib:
    smtplib.login(email_sender, email_password)
    smtplib.sendmail(email_sender, email_receiver, em.as_string())
