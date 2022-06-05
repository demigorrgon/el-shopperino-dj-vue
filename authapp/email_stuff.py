import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_msg(server, port, login, password, receiver, subject, message):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = login
    msg["To"] = receiver

    text = MIMEText(message, "plain")
    msg.attach(text)
    s = smtplib.SMTP(server, port)
    s.starttls()
    s.login(login, password)
    print("auth starts")
    # return "logged in i guess"
    s.sendmail(login, receiver, msg.as_string())
    # print("sent")
    s.quit()
    return "Success"
