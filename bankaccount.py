import datetime
import pytz


class Account:
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []

        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((Account._current_time(), amount))
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), amount))
        else:
            print("You broke, bitch.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}.".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))



if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.show_transactions()
