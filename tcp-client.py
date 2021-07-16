" Created by Ecem Balıkçı on 5/20/2021 at 3:39 PM (Contact: balikciecem@gmail.com) "
import socket

if __name__ == "__main__":
    HOST ="127.0.0.1"
    PORT = 8642

# client = MyClient()
# client.deposit(20)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))

    string = input("Enter message")
    server.send(bytes(string, "utf-8"))  # send message to server now go back to server file
    buffer = server.recv(1024)  # receive message from server
    buffer = buffer.decode("utf-8")
    print(f"Server says:{buffer}")