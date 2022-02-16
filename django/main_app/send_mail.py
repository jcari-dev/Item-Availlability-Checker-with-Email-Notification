from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')


def sendMail(send_to, subject_to, body_to):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_USER, EMAIL_PASS)
        
        my_email = MIMEText(body_to, "html")
        my_email["From"] = EMAIL_USER
        my_email['To'] = send_to
        my_email['Subject'] = subject_to

        # subject = subject_to
        # body = body_to
        
        # server = smtplib.SMTP(my_server)

        # msg = f'Subject: {subject}\n\n{body}'

        # return smtp.sendmail(EMAIL_USER, send_to, msg)
        return smtp.sendmail(EMAIL_USER, send_to, my_email.as_string())
