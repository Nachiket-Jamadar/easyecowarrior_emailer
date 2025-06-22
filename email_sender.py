import os
import smtplib
from email.message import EmailMessage
from email_generator import generate_email

def send_generated_email(subject, body, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'your_email_id_here' # Use this mail to generate App password
    password = os.getenv('EMAIL_APP_PASSWORD')  # Load from env variable

    if not password:
        raise Exception("Environment variable EMAIL_APP_PASSWORD is not set")

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Cc'] = 'nachiketjam@gmail.com'
    msg.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        print(f"Email sent to {to_email}!")

def send_email(company):
    recipient = company.split('\n')[1]
    mail_content = generate_email(company.split('\n')[1])
    mail_body = mail_content['body'].replace("*",'')
    mail_subject = mail_content['subject'].replace("*",'')
    send_generated_email(mail_subject, mail_body, recipient)

    print(mail_subject)
    print(mail_body)

