from email.messege import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'email@email.com'
email_password = password

email_receiver = ''

subject = "dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

em = Emailmessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)