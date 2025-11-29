import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "sureshsvi1975@gmail.com"
APP_PASSWORD = "pwry sgav tnxb ooof"
RECEIVER = "sureshchoyal629@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "helllo For python ......."
msg.set_content("this email was shared by python code ......")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
    
    
    
    
    