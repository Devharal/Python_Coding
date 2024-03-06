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
        self.__pin=""  #__ to make this variable priavte
        self.__balance=0
        print(id(self))  #Self kya hai ->will give some address id(sbi)(->object)
        self.__menu()

    def get_pin(self): # getter and setter functions
        return self.__pin
    
    def set_pin(self,new_pin):
        self.__pin=new_pin
        print("Pin changed")

        return
    def __menu(self):  #method ko bhi chupa sakte  
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
        self.__pin=input("Enter your pin: ")
        print("Pin set Successfuly: ")
    def deposit(self):
        temp=input("Enter you pin: ")
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            self.__balance=self.__balance+amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")
    def withdraw(self):
        temp=input("Enter you pin")
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("Operation Done: ")
            else:
                print("Paisa nahi hai ")
        else:
            print("Invalid Pin")


# sbi=Atm()
# sbi.deposit()
# sbi.withdraw()
# print(id(self))  #Self kya hai ->will give some address id(sbi)(->object)
# sbi hi self hai jis object ke sath abhi kam kr rahe ho wo self hai
# so basically hum object ko pass kr rahe methods mai lekin q
# oops fundamental hai ki class mai methods or data hota hai
# aur in data or method ko bs object access kr sakta
# class mai khud ek method dusre method call nhi kr sakt isliye self use krte
class Fraction:
    # Instance Variable-> varible called inside constructor,for which value of variable is different for diff object
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):  #ye magic fuction tab excute hota jab bhi hum kuch rint krna chahte hai
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):
        temp_num=self.num*other.den + other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    
x=Fraction(4,5)
y=Fraction(3,5)
print(type(x))
print(x)
print(x+y)
print(x*y)

