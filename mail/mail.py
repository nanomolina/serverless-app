import json
import os
import smtplib
from email.mime.text import MIMEText


def lambda_handler(event, context):
    SMTP_USERNAME = os.environ['SMTP_USERNAME']
    SMTP_PASS = os.environ['SMTP_PASS']

    # Get body
    body_str = event.get('body', '')
    body_str = body_str.replace('\\n', r'\\n')
    body = json.loads(body_str)

    # Email details
    sender_email = body.get('email', 'email@default.com')
    receiver_email = SMTP_USERNAME
    name = body.get('name', 'name')
    subject = body.get('subject', 'Test Email')
    message = body.get('message', '')
    try:
        # Create a MIMEText object
        header = f'This is a message from {name}\n'
        message = header + message
        email_body = MIMEText(message)

        # Set email details
        email_body['Subject'] = subject
        email_body['From'] = sender_email
        email_body['To'] = receiver_email

        # SMTP server configuration
        smtp_server = 'smtp.example.com'
        smtp_port = 587

        # Create an SMTP connection
        smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
        smtp_conn.starttls()
        smtp_conn.login(SMTP_USERNAME, SMTP_PASS)

        # Send the email
        smtp_conn.sendmail(sender_email, receiver_email, email_body.as_string())

        # Close the SMTP connection
        smtp_conn.quit()
    except Exception:
        response = 'Try again'
    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
    }