import smtplib
from email.mime.text  import MIMEText

body="this is a test email. how are you"

msg= MIMEText(body)
msg['From']="abhisek.khuntia16@gmail.com"
msg['To']="abhisek.khuntia16@gmail.com"
msg['Subject']="Hello"

server= smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("abhisek.khuntia16@gmail","mikoyan35")

server.send_message(msg)

print("Mail Sent")

server.quit()