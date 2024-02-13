class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to the {receipient} successfully.")
        else:
            print("Sorry you have Insufficient balance. ")

    def check_balance(self):
        print(f"Current balance: {self.account_balance} KES")


class Personal_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id = id_number

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} airtime successfully purchased.")
        else:
            print("Sorry you have Insufficient balance.")

    def check_balance(self):
        print(f"Current balance: {self.account_balance} KES")


class Business_mpesa(Personal_Mpesa):
    def __init__(self, account_balance, phone_number, id_number, business_name):
        super().__init__(account_balance, phone_number, id_number)
        self.bussiness_name = business_name

    def receive_money(self, amount):
        self.account_balance += amount
        print(f"{amount} Kes received successfully from {self.bussiness_name}.")

    def check_balance(self):
        print(f"Current balance: {self.account_balance} KES")


personal = Personal_Mpesa(
    account_balance=800, phone_number=254722000000, id_number=35678900
)
personal.send_money(550, 254722890890)
personal.buy_airtime(amount=50)

business = Business_mpesa(
    account_balance=5000,
    phone_number=2547234567,
    id_number=255267890,
    business_name="Mohammed Amin",
)
business.receive_money(2000)

# Additional transactions
personal.send_money(50, 25428990890)
business.receive_money(2000)
personal.buy_airtime(100)


personal.check_balance()
business.check_balance()
