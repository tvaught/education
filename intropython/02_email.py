#!/usr/bin/env python3

# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage


msg = EmailMessage()
msg['Subject'] = 'Test Email from Python'
msg['From'] = 'travis@vaught.net'
msg['To'] = 'vaught.travis@gmail.com'
msg.set_content(""" This is a test email.
It is being sent by a python script.
""")

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost', 1025)
s.send_message(msg)
s.quit()
