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
    # this private data,getter and setter together form concept called Encapsulation
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
            
# Here we make our own DATATYPE called Fraction 
class Fraction:
    # Instance Variable-> varible called inside constructor,for which value of variable is different for diff object
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):  #ye magic fuction tab excute hota jab bhi hum kuch rint krna chahte hai
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):       #There are many such magic such used for building various datatypes
        temp_num=self.num*other.den + other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    
# x=Fraction(4,5)
# y=Fraction(3,5)
# print(type(x))
# print(x)
# print(x+y)
# print(x*y)

# Reference variable
# Atm() we have not stored this object so it has lost
# sbi=Atm()  sbi ek variable jo point krta hai jaha actual address hai
# sbi is reference variable and Atm() is object call krke
class Customer:

    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(customer):
    if customer.gender=="Male":
        print("Hello ",customer.name,"Sir")
    else:
        print("Hello ",customer.name,"Mam")

# cust=Customer("Dev","Male")
# greet(cust)
# Pass by reference
class Customer2:
    def __init__(self,name):
        self.name=name
def greet(customer):
    print(id(customer))
    customer.name="Hrishi"
    print(customer.name)
    print(id(customer))

# cust=Customer2("Dev")
# print(id(cust))
# greet(cust)

# print(cust.name)
# class ke object are also mutable like lists,dictionary and sets
# edit krne bad bhi id same rehti hai like same jagah update hota hai object
# lekin ye cheez tuple mai alg hai update ke bad id change hoti hai

# Collection of Object
    
class Customer3:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print("I am",self.name,"and I am",self.age)
c1=Customer3("Dev",2)
c2=Customer3("Dev2",3)
c3=Customer3("Dev3",4)

L=[c1,c2,c3]

# for i in L:
#     i.intro()

# STATIC
# Hamesha constructor ke bahar hota hai while instance variable construtor ke andr hota hai

class Atm2():

    __counter=1 # declaring an static variable
    def __init__(self): 
        self.__pin=""  
        self.__balance=0
        self.sno=Atm.counter
        Atm.__counter=Atm.__counter+1
        print(id(self))  
        self.__menu()

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__counter==new
        else:
            print(Atm.counter)

    def get_pin(self): 
        return self.__pin
    
    def set_pin(self,new_pin):
        self.__pin=new_pin
        print("Pin changed")


# Multiple Classes relationship between this classes
# 1. Aggregation(has-A) and 2. Inheritance(In-A)
# Car Is-A Vehicle
# Customer Has-A address 

class Customer4:

    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state)

class Address:

    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    def change_address(self,new_city,new_pin,new_state):
        self.new_city=new_city
        self.new_pin=new_pin
        self.new_state=new_state

# add=Address("Nanded",431605,"MH")
# cust55=Customer4("Dev","Male",add)

# cust55.edit_profile()
# print(cust55.address.city)
        
# INHERITANCE
# DRY->DONT REPEAT YOURSELF
# Code Reusability - Saves time code consize hai
# down up approach is done in inheritance
# Private members are not inherited
class User:
    # parent class
    def login(self):
        print("Login")
    def register(self):
        print("Register")

class Student(User):
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

# stu1=Student()
# stu1.enroll()
# stu1.login()
# stu1.register()
# stu1.review()

# Method overriding
class Phone:
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self): #same method in both classes
        print("Buy karu kya")

class SmartPhone(Phone):

    def buy(self): #but when call object of this class with buy method it will output this classes method
        print("buy smartphone")

# SUPER

class Phone2:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("buying a phone")

class SmartPhone2(Phone2):

    def buy(self):
        print("Buying a smartphone")
        super().buy() #parent ka buy method use kr sakte

# s=SmartPhone2(2000,"Apple",13)
# s.buy()  #Method Overriding using super we can use parent ka buy method
# Super class ke bahr use nhi kr sakte ,super se parent ke method aur parent ke constructor access kr sakte
# Badshah Example

class Phone3:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera


class SmartPhone3(Phone3):
    
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("Inside samrtphone")

s11=SmartPhone3(2000,"Samsung",12,"Android",2)
# print(s11.os)
# print(s11.brand)

# Type of Inheritance
# 1.Single level inheritance
# 2.Multi Level 
# 3.Hierarchical
# 4. Multiple Inheritance  (not in Java)
# 5. Hibrid Inheritance ->combination of various inheritance 


# POLYMORPHISM
# 1. Method Overriding
# 2. Method Overloading
# 3. Operator Overloading

class Geometry:

    def area(self,radius):
        return 3.14*radius*radius
    
    def area(self,l,b):
        return l*b
obj=Geometry()
print(obj.area(4))
# Ek method ko alg input de rahe hai