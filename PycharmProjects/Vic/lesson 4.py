class Account:
    # Create a constructor
    # below we initialize the object
    def __init__(self, accno,amount,name,type):
        self.ac = accno
        self.am = amount
        self.nam = name
        self.typ = type

    # deposit should parse a parameter to allow hold deposited cash
    def deposit(self, depamount):
        if depamount < 50:
            print("Below Deposit Threshold!")
        else:
            self.am = self.am + depamount
            print("Deposit of ", depamount,"Successful")


    def withdraw(self, withdrawn):
       if withdrawn > self.am:
           print("Insufficient funds!!!")
       else:
           self.am = self.am - withdrawn
           print("Withdrawal of", withdrawn, "Successful")


    def checkdetails(self):
        answer = input("Would you like to check your account details? Y or N")
        if answer is 'Y':
            print("-----Account Details.-----")
            print(self.ac)
            print(self.typ)
            print(self.nam)
            print(self.am)
        else:
            print("Goodbye!")


    def changetype(self):
        answer = input("Would you like to change your account type? Y or N")
        answer2 = input("Which letter would you like to choose? P, B or S")
        account_types = ("Personal, Business, Savings")
        if answer is 'Y':
            print("Change your accout to", account_types)

        else:
            print("Goodbye!")







    def checkbalance(self):
        print("Current Balance ", self.am)


# create the account object
ob = Account(10003,50000,"Joe","Personal")
ob.deposit(40000)
ob.deposit(20000)
ob.deposit(50000)
ob.deposit(40)
ob.withdraw(150000)
ob.withdraw(15000)
ob.deposit(100000)
ob.withdraw(50000)
ob.checkbalance()
ob.checkdetails()
ob.changetype()


