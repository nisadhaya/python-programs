import smtplib
import os
import time
from datetime import datetime
from email.message import EmailMessage
SENDER_EMAIL = "yourgmail.com"
APP_PASSWORD = "your password"

RECEIVER_EMAIL = "yourgmail.com"

SUBJECT = "Scheduled Email from Python"
BODY = """
Hello,

This email was automatically sent using Python SMTP Timer.

Regards,
Python Automation
"""

FILE_PATH = r"C:\Users\c2c.ITNT64\Desktop\addition.py"

SEND_TIME = "14:16"

print("Waiting for scheduled time:", SEND_TIME)
while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == SEND_TIME:
        print("Time Matched! Sending Email...")
        break

    time.sleep(30)
msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = SUBJECT

msg.set_content(BODY)
try:
    with open(FILE_PATH, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(FILE_PATH)

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name
        )

    print("File Attached Successfully!")

except FileNotFoundError:
    print("File Not Found!")
    exit()
try:
    print("Connecting to Gmail SMTP...")

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(SENDER_EMAIL, APP_PASSWORD)

    print("Login Successful!")

    server.send_message(msg)

    print("Email Sent Successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()
    print("SMTP Server Closed.")
