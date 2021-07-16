" Created by Ecem Balıkçı on 5/20/2021 at 11:23 AM (Contact: balikciecem@gmail.com) "
import socket
import threading, queue


class MyServer:
    balance = 1000

    def deposit(self):

        message = f"Total amount of money you have: {self.balance}".encode()
        client.send(message)
        amount_ = client.recv(1024)
        amount_int = int(amount_)
        self.balance += amount_int
        client.send(f"Deposit successful, total amount of money you have: {self.balance}".encode())

    def withdraw(self):

        client.send(f"Total amount of money you have: {self.balance}".encode())
        amount_ = client.recv(1024)
        amount_int = int(amount_)
        if amount_int >= self.balance:
            client.send("Not enough credit!".encode())
        else:
            self.balance -= amount_int
            client.send(f"Withdraw successful, total amount of money you have: {self.balance}".encode())

    def menu(self):

        choice_ = client.recv(1024)
        choice_int = int(choice_)
        while choice_int != 0:

            if choice_int == 1:
                print("Client chose: ", choice_int)
                self.deposit()
            elif choice_int == 2:
                print("Client chose: ", choice_int)
                self.withdraw()
            elif choice_int == 0:
                print("Client chose: ", choice_int)
                print('--------------------QUIT---------------------------')
                client.close()
                server.close()

        print("")


if __name__ == "__main__":
    HOST ="127.0.0.1"
    PORT = 8642
    clientList = []
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    while True:

        client, address = server.accept()
        print("Connected by ", address)
        clientList.append(client)
        atm = queue.Queue()
        client_ = atm.get()
        if len(clientList) == 1:
            MyServer().menu()
        elif len(clientList) >= 1:
            client.send(f"ATM is busy, please wait.".encode())
            threading.Thread(target=MyServer, daemon=True).start()
            atm.put(client_)
            atm.join()