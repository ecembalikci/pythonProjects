" Created by Ecem Balıkçı on 5/20/2021 at 3:39 PM (Contact: balikciecem@gmail.com) "
import socket
if __name__ == "__main__":
    HOST ="127.0.0.1"
    PORT = 8642

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    while True:
        client, address = server.accept()
        print("Connected by ", address)  # {address[0]}:{address[1]}

        string = client.recv(1024) #receive messages from client
        string=string.decode("utf-8")
        client.send(bytes(string, "utf-8")) #send message to client now go back to client file
        client.close()