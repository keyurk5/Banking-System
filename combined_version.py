
            
class Bank:
    def __init__(self):
        self.ifsc_code = 111
        self.bankname = 'BOB'
        self.branchname = '7th street'
        self.loc = 'LA'
        
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
            print("Insufficient Balance to withdraw")

    def getbalance(self):
        print("Your Account Balance is " + str(self.balance))
        return self.balance

    def getaccountinfo(self):
        return 'Customer ID - ' + str(self.customer.customerid) + '\n' \
               'Customer Name - ' + self.customer.custname + '\n' \
               + 'Bank Account ID - ' + str(self.accountID) + '\n' \
               'Bank Name - ' + self.bankname + '\n' \
               'Bank balance - ' + str(self.balance)
               
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
class Customer:
    def __init__(self, customerid, custname, address, contactdetails):
        self.customerid = customerid
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails
        
class Run:
    def __init__(self):
        while (1) :
            print("-----Please select following options: ------\n")
            customer_status = int(input("1) Create Customer \n 2) Existing Customer \n"))
    
            if customer_status == 1:
                print("-----Please Enter the Customer Details------")
                customerid = int(input("Please enter customer id: "))
                custname = input("Please enter customer name: ")
                address = input("Please enter customer address: ")
                contact = int(input("Please enter customer contact details: "))
                accountid = int(input("Please enter bank account id: "))
                
                # create object for cusomer
                # customer = Customer(customerid, custname, address, contact)
                
                # create object for bank
                self.account = Savingsaccount(accountid, customerid, custname, address, contact)
                self.function()
            else:
                print("Exisitng Customer:")
                self.function()
                
    def function(self,):
        while (1) :
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
        deposit_amount = int(input("Enter Amount to be deposited:"))
        self.account.deposit(deposit_amount, 'true')
        print("deposited amount")
     

    def withdraw(self):
        print("Withdraw Balance:")
        withdrawn_amount = int(input("Enter Amount to be withdrawn:"))
        self.account.withdraw(withdrawn_amount)
        self.getbalance()
     

    def getbalance(self):
        print("Getting balance")
        self.account.getbalance()



Run()
