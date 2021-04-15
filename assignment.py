from savingsaccount import Savingsaccount
from customer import Customer


class Run:
    def __init__(self):
        print("-----Please select following options: ------\n")
        customer_status = int(input("1) Create Customer \n 2) Existing Customer \n"))

        if customer_status == 1:
            print("-----Please Enter the Customer Details------")
            self.customerid = int(input("Please enter customer id: "))
            self.custname = input("Please enter customer name: ")
            self.address = input("Please enter customer address: ")
            self.contact = int(input("Please enter customer contact details: "))
            self.accountid = int(input("Please enter bank account id: "))
            customer_dict = {self.customerid: Customer(self.customerid, self.custname, self.address, self.contact)}
            self.function()
        else:
            print("-----Please Enter the Customer Details------")
            # self.customerid = int(input("Please enter customer id: "))
            # self.custname = input("Please enter customer name: ")
            # self.address = input("Please enter customer address: ")
            # self.contact = int(input("Please enter customer contact details: "))
            # self.accountid = int(input("Please enter bank account id: "))
            # self.account = Savingsaccount(self.accountid, self.balance, self.customerid, self.custname, self.address,
            #                 self.contact, self.ifsc_code, self.bankname, self.branchname, self.loc, self.minbalance)
            # self.function()

    def function(self):
        operation = int(input("Please enter the operation you want to perform: \n 1) Deposit \n 2) Withdraw \n 3) Show Balance \n 4) Exit "))
        if operation == 1:
            self.deposit()

        elif operation == 2:
            self.withdraw()

        elif operation == 3:
            self.getbalance()
        else:
            exit()

    def deposit(self):
        self.account = Savingsaccount(self.accountid, self.customerid, self.custname, self.address, self.contact)
        deposit_amount = int(input("Enter Amount to be deposited:"))
        self.account.deposit(deposit_amount, 'true')
        self.function()

    def withdraw(self):
        withdrawn_amount = int(input("Enter Amount to be withdrawn:"))
        self.account.withdraw(withdrawn_amount)
        self.function()

    def getbalance(self):
        self.account.getbalance()
        self.function()


Run()
