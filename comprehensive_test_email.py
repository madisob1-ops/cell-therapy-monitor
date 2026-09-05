#!/usr/bin/env python
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def send_test_email():
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL', 'madisob1@gene.com')
    
    print("=" * 80)
    print("CELL & GENE THERAPY MONITOR - EMAIL TEST")
    print("=" * 80)
    print(f"Sender: {sender_email}")
    print(f"Recipient: {recipient_email}")
    
    if not sender_email or not sender_password:
        print("ERROR: Email credentials not set!")
        return False
    
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = "Cell & Gene Therapy Monitor - Test Email"
        message["From"] = sender_email
        message["To"] = recipient_email
        
        html = """
        <html>
        <body>
        <h1>Cell & Gene Therapy Monitor</h1>
        <p>Your monitoring system is active!</p>
        <p>Monitoring:</p>
        <ul>
        <li>CAR-T Cell Therapy</li>
        <li>DNA-LNP Gene Therapy</li>
        <li>High-Impact Publications</li>
        <li>M&A and Funding</li>
        </ul>
        <p>Test email sent: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC') + """</p>
        </body>
        </html>
        """
        
        html_part = MIMEText(html, "html")
        message.attach(html_part)
        
        print("Sending email...")
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [recipient_email], message.as_string())
        
        print("SUCCESS! Email sent!")
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    success = send_test_email()
    sys.exit(0 if success else 1)
