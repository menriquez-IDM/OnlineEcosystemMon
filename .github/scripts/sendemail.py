import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def send_email(sender_email, sender_password, recipient_email, subject, message):
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

# # Example usage
# sender_email = 'your-email@gatesfoundation.org'  # Replace with your email address
# sender_password = 'your-email-password'  # Replace with your email password
# recipient_email = 'recipient-email@gatesfoundation.org'  # Replace with recipient's email address
# subject = 'Hello from the monitoring GHA'
# message = 'This is the body of the email.'

send_email(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


