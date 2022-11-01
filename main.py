import smtplib
import ssl
from email.message import EmailMessage


email_sender = '******************'  #Your email address
email_password = '*************' # Your app passwords

email_receiver = '************' #mail the one you want to send

subject = "Dont forget  to subscribe"

body = """ Lorem 100 """


em = EmailMessage
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

# setting with google smtp
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
