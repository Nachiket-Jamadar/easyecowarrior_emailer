import os
import smtplib
from email.message import EmailMessage
from email_generator import generate_email


company = '''
Jain College of Engineering and Technology, Hubballi
nachiketjam@gmail.com'''

def send_email(subject, body, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'nachiketrjamadar@gmail.com'
    password = os.getenv('EMAIL_APP_PASSWORD')  # Load from env variable

    if not password:
        raise Exception("Environment variable EMAIL_APP_PASSWORD is not set")

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        print(f"Email sent to {to_email}!")

recipient = company.split('\n')[1]
mail_content = generate_email(company.split('\n')[1])
mail_body = mail_content['body'].replace("*",'')
mail_subject = mail_content['subject'].replace("*",'')

print(mail_subject)
print(mail_body)

# Example
# send_email(mail_subject, mail_body, recipient)
