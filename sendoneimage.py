import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import imghdr

# Load environment variables
load_dotenv()

email_id = os.getenv("EMAIL_ADOR")
email_pass = os.getenv("EMAIL_PASS")

msg = EmailMessage()
msg['Subject'] = 'Manifestation'
msg['From'] = email_id
msg['To'] = 'vemurinikethana@gmail.com'
msg.set_content('Prabhat and I will get a job very soon and 2025 is going to be an amazing year for Prabhat and me.')

with open('.venv/img.png', 'rb') as m:
    file_data = m.read()
    file_type = imghdr.what(m.name)
    file_name = m.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

if not email_id or not email_pass:
    raise ValueError("EMAIL_ADOR and EMAIL_PASS environment variables must be set.")

# Send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)

print("Email sent successfully!")
