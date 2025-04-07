#oops

#class is a blue print
"""
class Car():
    car_color="blue"
    brand="mercedez"

obj1=Car()
print(obj1.car_color)
print(obj1.brand)
"""

#constructors
#init function (constructor) when object is created init function is automatically invoked
#the self parameter is reference to the current instance of the class and is used to access variables that belongs to the class

"""
class student():
    name="devesh"
    def __init__(self,name,age):
        self.name=name
        self.age=age


obj1=student("devesh",21)
print(obj1.name)
print(obj1.age)

obj2=student("jeevansh",90)
print(obj2.name)
print(obj2.age)
"""
"""
class Learning():

    #default constructor 
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self,vehicalcolor,vehicaltype):
        self.vehicalcolor=vehicalcolor
        self.vehicaltype=vehicaltype


ob = Learning("black","petrol")
print(ob.vehicalcolor,ob.vehicaltype)
"""

#CLASS $ INSTANCE ATTRIBUTES
"""
class Vegetables():
    name="cauliflower"

#here higher preference will be give to object attribute no class attribute will run
    def __init__(self,name,type):
        self.name=name
        self.type=type

obb = Vegetables("spinach","leafy")
print(obb.name,obb.type)
"""

#METHODS
#methods are functions that belongs to objects
"""
class Vegetables():
    name="cauliflower"

#here higher preference will be give to object attribute no class attribute will run
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def welcome(self):
        print("this vegetables is tasty whic is",self.name)

    def typeof(self):
        print("this vegetables is tasty whic is type of",self.type)

obb = Vegetables("spinach","leafy")
print(obb.name,obb.type)
obb.welcome()
obb.typeof()
"""

#create student class that takes name ,marks of 3 subjects as a argument in constructor.
#then create a method to print the average
"""
class Student():
    def __init__(self):
        pass

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_average(self):
        sum=0
        for val in self.marks:
            sum=sum+val
        print(f"hi,{self.name} your average score is:",sum/3)


s1=Student("dvesh",[45,89,90])
print(s1.name,s1.marks)
s1.get_average()
"""

#STATIC METHODS
#METHODS THAT DONT USE THE SELF PARAMETER (WORK AT THE CLASS LEVEL)
#decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
#without permentaly modifying it.

"""
class Student():
    def __init__(self):
        pass

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod
    def hello():
        print("hello world")

    def get_average(self):
        sum=0
        for val in self.marks:
            sum=sum+val
        print(f"hi,{self.name} your average score is:",sum/3)


s1=Student("dvesh",[45,89,90])
print(s1.name,s1.marks)
s1.hello()
s1.get_average()

"""
# 2 Pillars of oops ----> ABSTRACTION / ENCAPSULATION

#ABSTRACTION -->  hiding the implementation details of a class and only showing the essential features to the user.
#abstract means to hide 
"""
class Car():
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("car started")

    def stop(self):
        self.brk=True
        print("car stopped")

carz=Car()
carz.start()
carz.stop()
"""

#ENCAPSULATION --> wrapping data and functions into a single unit


#inheritence --> 


#polymorphism --> 


# Q1 Create a account class with 2 attributes - balance & account no.

class Account():
    def __init__(self):
        pass

    def __init__(self,name,balance,account_no):
        self.name=name
        self.balance=balance
        self.account_no=account_no

    def credit(self,amount):
        self.balance += amount
        print("rs. ",amount,"was credited from your account")
        print("total balance = ",self.finalbalance())

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited from your account")
        print("total balance = ",self.finalbalance())


    def finalbalance(self):
        return self.balance

acc=Account("devesh",10000,1234)
print(acc.name,acc.balance,acc.account_no)
acc.credit(20000)
acc.debit(1000)


















 

