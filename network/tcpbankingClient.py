" Created by Ecem Balıkçı on 5/20/2021 at 11:23 AM (Contact: balikciecem@gmail.com) "
import socket
import tcpbankingServer


class MyClient:
    balance_ = tcpbankingServer.MyServer().balance


    def deposit(self):
        balance_msg = server.recv(1024)
        balance_msg = balance_msg.decode("utf-8")
        print(f"Server says:{balance_msg}")
        amount = int(input("The amount you want to deposit: "))
        server.send(bytes(amount))
        d_msg = server.recv(1024)
        print(f"Server says:{d_msg}")

    def withdraw(self):
        amount = str(input("The amount you want to withdraw: "))
        server.send(bytes(amount, "utf-8"))
        w_msg = server.recv(1024)
        print(f"Server says:{w_msg}")

    def menu(self):

        print("---------------Welcome to Ecem's Bank!------------------")
        print("Press 1 to DEPOSIT MONEY")
        print("Press 2 to WITHDRAW MONEY")
        print("Press 0 to QUIT")
        print("--------------------------------------------------------")
        choice = 1000

        while choice != '0':

            choice = input("Please choose your option: ")
            server.send(bytes(choice, "utf-8"))
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '0':
                print('--------------------QUIT---------------------------')
            else:
                print("Option invalid, please try again.")
        print("")


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8642

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))

    client = MyClient()
    client.menu()