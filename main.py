import smtplib
import ssl
from email.message import EmailMessage


email_sender = '******************'
email_password = '*************'

email_receiver = 'farhodg7463@gmail.com'

subject = "Dont forget  to subscribe"

body = """ When you weatach vide please hgis asasd Farhid """


em = EmailMessage
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
