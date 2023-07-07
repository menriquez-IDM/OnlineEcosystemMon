import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Change this for other email providers
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

# Example usage
sender_email = 'your-email@gmail.com'  # Replace with your email address
sender_password = 'your-email-password'  # Replace with your email password
recipient_email = 'recipient-email@example.com'  # Replace with recipient's email address
subject = 'Hello from Python!'
message = 'This is the body of the email.'

send_email(sender_email, sender_password, recipient_email, subject, message)


