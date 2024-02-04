import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

sender_email = "*********************"
sender_password = "***************"

# Recipient email
recipient_email = "*********************"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Challenge 3 Completed"
body = """
Your name: Khushboo
Semester: 4th
Branch: MCA
Roll number: 22MCA20840
"""

message.attach(MIMEText(body, "plain"))
file_path = "C:/Users/khush/Documents/Python_Programs/Email_Send/Formal.jpg"
file_name = "Formal.jpg"

with open(file_path, "rb") as file:
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", f"attachment; filename={file_name}")
    message.attach(attachment)
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
   