class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, receipent):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES has been sent successfully to {receipent}")
        else:
            print("Sorry you have insuffucient balance")

    def check_balance(self):
        print(f"Current balance: {self.account_balance} KES")


class Personal_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id = id_number

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} airtime has been succesfully purchased.")
        else:
            print("Sorry you have insufficient balance!")

    def check_balance(self):
        print(f"Current Balance: {self.account_balance} KES")


personal = Personal_Mpesa(
    account_balance=2000, phone_number=254723567890, id_number=25678900
)
personal.send_money(1500, 2547899000)
personal.buy_airtime(amount=1000)
personal.check_balance()
