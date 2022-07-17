import smtplib
from email.message import EmailMessage


def send_email(sender_mail, password, receivers_mail, subject, text):
    message = EmailMessage()
    message.set_content(text)
    message["Subject"] = subject
    message["From"] = sender_mail
    message["To"] = receivers_mail
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        smtp_obj.starttls()
        smtp_obj.ehlo()
        smtp_obj.login(sender_mail, password)
        smtp_obj.sendmail(sender_mail, receivers_mail, str(message))
        print("Successfully sent email")
    except Exception as e:
        print(repr(e))
