from customer import Customer
from bank import Bank


class Account(Bank):
    def __init__(self, accountid, customerid, custname, address, contactdetails):
        super().__init__()
        self.accountID = accountid
        self.customer = Customer(customerid, custname, address, contactdetails)
        self.balance = 0

    def setbalance(self, amount):
        self.balance += amount
        print("self balance account - " + str(self.balance))

    def deposit(self, amount, status):
        if status:
            self.setbalance(amount)
            print("Amount Deposited Successfully..")
        return 0

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient Balance to withdraw. Minimum Balance should be 500.")

    def getbalance(self):
        print("Your Account Balance is " + str(self.balance))
        return self.balance

    def getaccountinfo(self):
        print('Customer ID - ' + str(self.customer.customerid) + '\n Customer Name - '
              + self.customer.custname + '\n Bank Account ID - ' + str(self.accountID) + '\n Bank Name - '
              + self.bankname + '\n Bank balance - ' + str(self.balance))
