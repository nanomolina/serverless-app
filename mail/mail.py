import json
import os
import smtplib
from email.mime.text import MIMEText


def lambda_handler(event, context):
    SMTP_USERNAME = os.environ['SMTP_USERNAME']
    SMTP_PASS = os.environ['SMTP_PASS']

    # Extract the request body from the event
    body_str = event['body']
    body_str = body_str.replace('\\n', r'\\n')
    body = json.loads(body_str)

    # Access the parsed form data
    name = body.get('name', 'No name')
    sender_email = body.get('email', 'No mail')
    receiver_email = SMTP_USERNAME
    subject = body.get('subject', 'Default subject')
    message = body.get('message', 'Default message')

    # Create a MIMEText object
    header = f'Name: {name}\n'
    header += f'Email: {sender_email}\n\n'
    message = header + message
    email_body = MIMEText(message)

    # Set email details
    email_body['Subject'] = subject
    email_body['From'] = sender_email
    email_body['To'] = receiver_email

    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create an SMTP connection
    smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
    smtp_conn.starttls()
    smtp_conn.login(SMTP_USERNAME, SMTP_PASS)

    # Send the email
    smtp_conn.sendmail(sender_email, receiver_email, email_body.as_string())

    # Close the SMTP connection
    smtp_conn.quit()

    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'OK'}),
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
    }