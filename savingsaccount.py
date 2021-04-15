from account import Account


class Savingsaccount(Account):
    def __init__(self, accountid, customerid, custname, address, contactdetails):
        super().__init__(accountid, customerid, custname, address, contactdetails)
        self.minbalance = 500

    def withdraw(self, amount):
        if (self.balance > amount) & ((self.balance - amount) >= self.minbalance):
            self.balance = self.balance - amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient Balance to be withdrawn")
