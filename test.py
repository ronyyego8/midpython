class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, receipent):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} has been successfully sent to {receipent}")
        else:
            print("Sorry you have insufficient funds.")

    def check_balance(self):
        print(f"Current balance : {self.account_balance} KES")
