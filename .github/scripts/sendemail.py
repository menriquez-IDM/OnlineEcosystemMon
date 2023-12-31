import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys, os


sender_email = sys.argv[1]
sender_password = sys.argv[2]
recipient_email = os.environ.get('RECIPIENT_EMAIL')
subject = os.environ.get('SUBJECT')
message = os.environ.get('MESSAGE')

print("Sender: ", sender_email)
print("Recipient: ", recipient_email)

# Set up the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

# Attach the message to the email
msg.attach(MIMEText(message, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP('smtp-relay.gmail.com', 587)  # Change this for other email providers
    server.starttls()

    # Log in to the sender's email account
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)
    print("Email sent successfully!")

except Exception as e:
    print(f"Error sending email: {str(e)}")

finally:
    # Disconnect from the SMTP server
    server.quit()

