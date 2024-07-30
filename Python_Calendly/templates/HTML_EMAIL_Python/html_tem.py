import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email content
sender_email = "your_email@example.com"
receiver_email = "recipient@example.com"
subject = "HTML Email Example"

# Create HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Email</title>
</head>
<body>
    <h2>Hello!</h2>
    <p>This is an HTML email example.</p>
    <p>Feel free to customize this template for your needs.</p>
    <p>Best regards,</p>
    <p>Your Name</p>
</body>
</html>
"""

# Create the MIME object
msg = MIMEMultipart()
msg["From"] = i
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach HTML content to the email
msg.attach(MIMEText(html_content, "html"))

# Send the email
try:
    smtp_server = smtplib.SMTP("smtp.example.com", 587)  # Replace with your SMTP server and port
    smtp_server.starttls()  # Secure the connection
    smtp_server.login(sender_email, "your_password")  # Replace with your email login credentials
    smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
    smtp_server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")