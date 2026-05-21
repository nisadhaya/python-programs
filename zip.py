import os
import smtplib
import time
import zipfile
from datetime import datetime
from email.message import EmailMessage
SENDER_EMAIL = "yourgmail.com"
APP_PASSWORD = "your password"
RECEIVER_EMAIL = "yourgmail.com"

SUBJECT = "Daily Folder Backup (Auto Zip)"
BODY = "Hi,\n\nThis is your daily automated backup.\n\nRegards,\nPython Bot"
FOLDER_PATH = r"C:\Users\c2c.ITNT64\Desktop\day 1"
ZIP_NAME = "backup.zip"
ZIP_PATH = os.path.join(FOLDER_PATH, ZIP_NAME)
SEND_TIME = "14:25"

print("Automation started... Waiting for time:", SEND_TIME)
def create_zip():
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(FOLDER_PATH):
            for file in files:
                file_path = os.path.join(root, file)

                # avoid zipping itself
                if file_path == ZIP_PATH:
                    continue

                zipf.write(file_path, arcname=file)

    print("ZIP Created:", ZIP_PATH)
while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == SEND_TIME:
        print("Time matched. Creating ZIP...")
        break

    time.sleep(30)
create_zip()
msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = SUBJECT
msg.set_content(BODY)
with open(ZIP_PATH, "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="application",
        subtype="zip",
        filename="daily_backup.zip"
    )

print("ZIP Attached")
try:
    print("Connecting SMTP...")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)

    server.send_message(msg)

    print("Email Sent Successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()
    print("SMTP Closed")
