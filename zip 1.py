import os
import smtplib
import time
import zipfile
from datetime import datetime
from email.message import EmailMessage

# =========================
# EMAIL CONFIG
# =========================

SENDER_EMAIL = "yourgmail.com"
APP_PASSWORD = "your password"
RECEIVER_EMAIL = "yourgmail.com"

SUBJECT = "Selected Day Backup"
BODY = "Hi,\n\nThis is your selected day file backup.\n\nRegards,\nPython Bot"

# =========================
# FOLDER PATH
# =========================

FOLDER_PATH = r"C:\Users\c2c.ITNT64\Desktop\day 4"
# =========================
# USER INPUT (DAY FILTER)
# Example: "2026-05-19"
# =========================

TARGET_DATE = "2026-05-19"

# =========================
# SCHEDULE TIME
# =========================

SEND_TIME = "15:19"

# ZIP FILE NAME
ZIP_NAME = f"backup_{TARGET_DATE}.zip"
ZIP_PATH = os.path.join(FOLDER_PATH, ZIP_NAME)

print("System started...")
print("Target Date:", TARGET_DATE)
print("Waiting for time:", SEND_TIME)

# =========================
# CREATE ZIP (ONLY SELECTED DAY FILES)
# =========================

def create_zip():
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zipf:

        for root, dirs, files in os.walk(FOLDER_PATH):
            for file in files:

                file_path = os.path.join(root, file)

                # skip zip itself
                if file_path == ZIP_PATH:
                    continue

                # get file modified date
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                file_date = file_time.strftime("%Y-%m-%d")

                # ONLY MATCH TARGET DATE
                if file_date == TARGET_DATE:
                    zipf.write(file_path, arcname=file)

    print("ZIP created for date:", TARGET_DATE)

# =========================
# WAIT FOR TIME
# =========================

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == SEND_TIME:
        print("Time matched...")
        break

    time.sleep(30)

# =========================
# CREATE ZIP
# =========================

create_zip()

# =========================
# EMAIL SETUP
# =========================

msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = SUBJECT
msg.set_content(BODY)

# =========================
# ATTACH ZIP
# =========================

with open(ZIP_PATH, "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="application",
        subtype="zip",
        filename=os.path.basename(ZIP_PATH)
    )

print("ZIP attached")

# =========================
# SEND EMAIL
# =========================

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)

    server.send_message(msg)

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()
    print("SMTP closed")
