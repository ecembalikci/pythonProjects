import socket
from cryptography.fernet import Fernet

f = Fernet(bytes('sqcyNL5kz2mxWb1KL2QSZWY-GCERE-scEgWBbvq9CCk=', "utf-8"))

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 65500
ss.bind((host, port))

while True:
    print("server is here and waiting for a client")
    msg_encrypted, addr = ss.recvfrom(2048)
    msg = f.decrypt(msg_encrypted, None).decode()
    print("client says:", msg, addr)
    if msg:
        msg_encode = msg.encode()
        msg_outgoing = f.encrypt(msg_encode)
        sent = ss.sendto(msg_outgoing, addr)
    else:
        ss.close()
