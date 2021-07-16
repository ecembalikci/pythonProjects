import socket
from cryptography.fernet import Fernet

f = Fernet(bytes('sqcyNL5kz2mxWb1KL2QSZWY-GCERE-scEgWBbvq9CCk=',"utf-8"))

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = ""
cs.connect(("127.0.0.1", 65500))

while msg != "exit":
    msg = str(input("enter message to send server: "))
    msg_encode = msg.encode()
    msg_encrypted = f.encrypt(msg_encode)
    cs.sendall(msg_encrypted)
    msg_income = cs.recv(2048)
    msg_decoded = f.decrypt(msg_income, None).decode()
    print("the response from server:", msg_decoded)

cs.close()
