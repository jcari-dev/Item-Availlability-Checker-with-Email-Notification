from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

def sendMail(send_to, subject_to, body_to):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        smtp.login(EMAIL_USER, EMAIL_PASS)
        
        subject = subject_to
        body = body_to
        
        msg = f'Subject: {subject}\n\n{body}'

        return smtp.sendmail(EMAIL_USER, send_to, msg)


print(EMAIL_USER)


