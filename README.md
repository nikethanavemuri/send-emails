# Email Automation Using Python

## Email Automation Scripts
This repository contains multiple Python scripts to automate email-sending tasks using the smtplib library. Each script demonstrates a unique functionality, from sending simple emails to sending emails with attachments and multiple recipients.

## Features
Send plain-text emails.
Send emails with single or multiple recipients.
Attach files of various types (e.g., images, PDFs).
Securely manage email credentials using environment variables.
Easy customization of email content, recipients, and attachments.

## Prerequisites
1) Python 3.x installed on your system.

2) Install required Python packages:
    pip install python-dotenv

3) A Gmail account configured for sending emails:

      Enable "Allow less secure apps" in your Gmail settings, or Use App Passwords for better security.

4) Create a .env file to store your credentials securely:
    EMAIL_ADOR=your_email@gmail.com
    EMAIL_PASS=your_app_password

## Scripts Overview
1. Basic Email Sending
Sends a plain-text email to a single recipient.
Example:
msg['Subject'] = 'Manifestation'
msg['From'] = email_id
msg['To'] = 'email1@gmail.com'
msg.set_content('Prabhat and I will get a job very soon, and 2025 is going to be an amazing year for Prabhat and me.')

2. Send Email with Single Image Attachment
Attaches an image to the email.
Example file: .venv/img.png
The script automatically detects the image type using the imghdr module.

3. Send Email with Multiple Image Attachments
Sends an email with multiple images attached.
Example files: .venv/img.png, .venv/img_1.png
Iterates through a list of image files to attach them.

4. Send Email with PDF Attachment
Attaches a PDF document to the email.
Example file: .venv/Resume_ChakrarajaNikethanaVemuri.pdf

5. Send Email to Multiple Recipients with Attachment
Sends an email to multiple recipients.
Attaches a file (e.g., resume or document) to the email.
Example recipients:
contacts = ['email1@gmail.com', 'email2@gmail.com']

## How to Run
Clone the repository:
git clone https://github.com/your-username/email-automation.git

cd email-automation

Add your email credentials to the .env file:
  EMAIL_ADOR=your_email@gmail.com
  EMAIL_PASS=your_app_password

Run the desired script:

## Acknowledgment
Special thanks to Techie Coder for their informative tutorials and guidance on email automation using Python. Their content served as an inspiration for creating these scripts.
