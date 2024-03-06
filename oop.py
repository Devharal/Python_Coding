# In Python everything is Object
# Helps to build real world application 
# Generality to Specificity
# Make our own datatype
# We will make our own datatype using OOPs

# CLASS and OBJECT
# object hoga toh wo kisi class ka hi hoga
# variable and object same maan sakte hai
# L=[1,2,3,4]
# See here list is class and L is object 
# When we do operation such as L.append,L.pop this are built function inside out list class
# Class ka naam should be in Pascal case
# Data and variable ka snakecase mai hoga
# CAR----->Wagor (object)  wagonr=Car() , 
# Object iternal easy method of making class
# Lets make class
#  ATM Machine
# Balance,deposit,ATM pin,create pin,withdraw
class Atm():
    # Function vs Methods(functions written inside class)
    # len(L)(->Function) len is function while l.append(x)(->Method)call krne ka tarif alg hai
    # Methods can only be accessed by its class
    def __init__(self): # init is construtor special method jiske andhar ka code automatically excute when this class is used
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input("""
                         Hello how would you like to proceed?
                         1. Enter 1 to create pin
                         2. Enter 2 to deposit
                         3. Enter 3 to withdraw
                         """)
        if user_input=="1":
            # print("Create Pin")
            self.create_pin()
        elif user_input=="2":
            # print("deposit")
            self.deposit()
        elif user_input=="3":
            # print("Withdraw")
            self.withdraw()
    
    def create_pin(self):
        self.pin=input("Enter your pin: ")
        print("Pin set Successfuly: ")
    def deposit(self):
        temp=input("Enter you pin: ")
        if temp==self.pin:
            amount=int(input("Enter the amount: "))
            self.balance=self.balance+amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")
    def withdraw(self):
        temp=input("Enter you pin")
        if temp==self.pin:
            amount=int(input("Enter the amount: "))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation Done: ")
            else:
                print("Paisa nahi hai ")
        else:
            print("Invalid Pin")


sbi=Atm()
sbi.deposit()
sbi.withdraw()