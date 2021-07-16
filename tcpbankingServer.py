" Created by Ecem Balıkçı on 5/20/2021 at 11:23 AM (Contact: balikciecem@gmail.com) "
import socket
import struct

class MyServer:
    balance = 1000

    def account(self):
        balance_message = f"Total amount of money you have: {self.balance}"
        client.send(bytes(balance_message, "utf-8"))

    def deposit(self):
        amount_ = client.recv(2)
        self.balance += amount_
        message_deposit = f"Deposit successful, total amount of money you have: {self.balance}"
        client.send(bytes(message_deposit, "utf-8"))

    def withdraw(self):
        amount_ = client.recv(2)
        if amount_ >= bytes(self.balance):
            message_error = "Not enough credit!"  # server
            client.send(bytes(message_error, "utf-8"))
        else:
            self.balance -= amount_
            message_success = f"Withdraw successful, total amount of money you have: {self.balance}"
            client.send(bytes(message_success, "utf-8"))

    def menu(self):
        choice_ = client.recv(2)
        if choice_.startswith(b'int'):
            # assumes 4 byte unsigned integer
            received = struct.unpack('!I', choice_[-4:])[0]
        else:
            received = choice_.decode('utf-8')
        print("Client chose: ", received)

        while received != '0':

            if received == '1':
                self.account()
                self.deposit()
            elif received == '2':
                self.account()
                self.withdraw()
            elif received == '0':
                print('--------------------QUIT---------------------------')
                client.close()

        print("")

if __name__ == "__main__":
    HOST ="127.0.0.1"
    PORT = 8642

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    while True:
        client, address = server.accept()
        print("Connected by ", address)
        myserver = MyServer()
        myserver.menu()


