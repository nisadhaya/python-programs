import os
import smtplib
from email.message import EmailMessage
sender_email = "yourgmail.com"
sender_password = "your password"
receiver_email = "yourgmail.com"
desktop_path = r"C:\Users\c2c.ITNT64\Desktop\factorial"
file_name = os.path.basename(desktop_path) 
msg = EmailMessage()
msg['Subject'] = "Desktop File Attachment From Python"
msg['From'] =  sender_email
msg['To'] = receiver_email
msg.set_content("Hi, Enoda Desktop-la irunthu anupunatha file itho intha mail-la attached-ah iruku. Check panni paarunga!")
try:
    print(f"Reading file from Desktop: {file_name}...")
    with open(desktop_path, 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    print("File attached successfully!")

except FileNotFoundError:
    print(f"❌ Error: Desktop-la '{file_name}' nu entha file-um illa! Path-ah check pannunga.")
    exit
try:
    print("Connecting to Gmail Server...")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  
        server.login(sender_email, sender_password)
        print("Login Successful! Sending Mail...")
        
        server.send_message(msg)
        print(f"🎉 Mail with '{file_name}' sent successfully!")

except Exception as e:
    print(f"❌ Error occurred: {e}")
