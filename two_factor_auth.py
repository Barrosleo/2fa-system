import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email Sending Function
def send_email(recipient_email, code):
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Your 2FA Code"

    body = f"Your 2FA code is: {code}"
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.example.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.close()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Generate 2FA Code
def generate_2fa_code():
    return random.randint(100000, 999999)

# Main Function to Implement 2FA
def two_factor_auth(recipient_email):
    code = generate_2fa_code()
    send_email(recipient_email, code)

    user_code = input("Enter the 2FA code sent to your email: ")
    if user_code == str(code):
        print("Authentication successful")
    else:
        print("Authentication failed")

# Test the Functions
if __name__ == "__main__":
    recipient_email = input("Enter your email: ")
    two_factor_auth(recipient_email)

