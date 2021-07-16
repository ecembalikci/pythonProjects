" Created by Ecem Balıkçı on 5/21/2021 at 12:20 AM (Contact: balikci8ecem@gmail.com) "


class MyClient:
    balance = 1000

    def deposit(self):

        balance_message = "Total amount of money you have: ", self.balance  # server
        print(balance_message)
        amount = int(input("The amount you want to deposit: "))
        self.balance += amount  # server
        message_deposit = "Deposit successful, total amount of money you have: ", self.balance  # server
        print(message_deposit)

    def withdraw(self):

        balance_message = "Total amount of money you have: ", self.balance  # server
        print(balance_message)
        amount = int(input("The amount you want to withdraw: "))
        if amount >= self.balance:
            message_error = "Not enough credit!"  # server
            print(message_error)
        else:
            self.balance -= amount
            message_success = "Withdraw successful, total amount of money you have: ", self.balance
            print(message_success)

    def menu(self):

        print("---------------Welcome to Ecem's Bank!------------------")
        print("Press 1 to DEPOSIT MONEY")
        print("Press 2 to WITHDRAW MONEY")
        print("Press 0 to QUIT")
        print("--------------------------------------------------------")
        choice = ''

        while choice != '0':

            choice = input("Please choose your option: ")
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '0':
                print('--------------------QUIT---------------------------')
            else:
                print("Option invalid, please try again.")
        print("")


if __name__ == '__main__':
    client = MyClient()
    client.menu()
