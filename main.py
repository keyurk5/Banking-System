from savingsaccount import Savingsaccount


class Run:
    def __init__(self):
        my_dict = {}

        while 1:
            print("----- Please select following options: ------\n")
            customer_status = int(input(" 1) New Customer \n 2) Existing Customer \n 3) Operations: \n"))

            # To create new customer
            if customer_status == 1:
                print("-----Please Enter the Customer Details------")
                customerid = int(input("Please enter customer id: "))
                custname = input("Please enter customer name: ")
                address = input("Please enter customer address: ")
                contact = int(input("Please enter contact details: "))
                accountid = int(input("Please enter the bank account id: "))

                self.account = Savingsaccount(accountid, customerid, custname, address, contact)
                my_dict[customerid] = self.account

            # For Existing Customer
            elif customer_status == 2:
                print("-----Please Enter the Customer Details------")
                customerid = int(input("Please enter customer id: "))
                if bool(my_dict):
                    self.account = my_dict[customerid]  # fetch dictionary customer id
                    print("Customer Found ")
                    self.function()
                else:
                    print("No Customers found")
            else:
                self.function()

    # Perform Deposit, withdraw, getbalance operations
    def function(self):
        while 1:
            operation = int(input("Please enter the operation you want to perform: \n 1) Deposit \n 2) Withdraw \n 3) Show Balance \n 4) Get Account Info \n 5) Exit \n"))
            if operation == 1:
                self.deposit()

            elif operation == 2:
                self.withdraw()

            elif operation == 3:
                self.getbalance()

            elif operation == 4:
                self.getaccountinfo()

            else:
                exit()

    def deposit(self):
        deposit_amount = int(input("Enter Amount to be deposited: "))
        self.account.deposit(deposit_amount, 'true')

    def withdraw(self):
        withdrawn_amount = int(input("Enter Amount to be withdrawn: "))
        self.account.withdraw(withdrawn_amount)
        self.getbalance()

    def getbalance(self):
        self.account.getbalance()

    def getaccountinfo(self):
        self.account.getaccountinfo()


Run()
