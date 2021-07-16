" Created by Ecem Balıkçı on 5/4/2021 at 12:23 PM (Contact: balikciecem@gmail.com) "

import smtplib
from email.mime.text import MIMEText

# writing a password into a script made no sense so I encrypted it in a .txt and read it via:
# (i did not include my password file while submitting cause i thought its unnecessary)
with open("pass.txt") as f:
    password = f.read()
# we can also take the password from user by password=input("Password: ")
# wrote nping --tcp -p 465 with my host address on command line and inspected it in Wireshark
mail_content = """
<b> Hello, my TCP packet response includes this information: </b>
      <p> Source Port: 40204 </p>
      <p> Destination Port: 465 </p>
      <p> Sequence Number: 0 </p>
      <p> Sequence Number (raw): 3086038046 </p>
      <p> [Next Sequence Number: 1    (relative sequence number)] </p>
      <p> Acknowledgment Number: 0 </p>
      <p> Acknowledgment number (raw): 0 </p>
      <p> 0101 .... = Header Length: 20 bytes (5) </p>
      <p> Flags: 0x002 (SYN) </p>
      <p> Checksum: 0x9cc6 [unverified] </p> 
      <p> [SEQ/ACK analysis] </p>
      <p> -->  [The RTO for this segment was: 1.013792000 seconds] </p>
      <p> [Timestamps] </p>
      <p> --> [Time since first frame in this TCP stream: 1.013792000 seconds] </p>
      <p> --> [Time since previous frame in this TCP stream: 1.013792000 seconds] </p>
      <p> Thank you. </p> 
      <p> Ecem Balıkçı</p> 
"""
# HTML tags are apparently working in python with 'html' in this case
message = MIMEText(mail_content, 'html')
message['FROM'] = 'mygmail@gmail.com'
message['TO'] = 'sendmail@gmail.com'
message['SUBJECT'] = 'a simple e-mail client'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Gmail SMTP port (SSL): 465
server.login('mygmail@gmail.com', password)  # used a dummy address to not face any security issues
server.sendmail('mygmail@gmail.com', 'sendmail@gmail.com', message.as_string())  # sender , receiver, message
server.quit()
