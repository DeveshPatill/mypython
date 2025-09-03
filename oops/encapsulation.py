#Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions.
#A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

# Python Class
# A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.

#warm up 
class Dog:
    bread = "labradog" #class attribute

    def __init__(self,name,age,owner_name):
        self.name=name
        self.age=age
        self.owner_name=owner_name

    """
    def owner(self):
        owner_name = input("enter the name: ")
        print(f"{owner_name} is the owner of {self.name}")
    """
    def owner(self):
        print(f"{self.owner_name} is the owner of the pet {self.name}")


obj=Dog("Troy",11,"Ishika")
print(obj.name)
print(obj.age)
print(obj.bread)
#print(obj.owner())
obj.owner()


#EXAMPLE 1
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
# ENCAPSULATION 
#Types of Encapsulation:
#Public Members: Accessible from anywhere.
#Protected Members: Accessible within the class and its subclasses.
#Private Members: Accessible only within the class.

class Dogg:
    def __init__(self,name,breed,age):
        self.name=name                  #public attribute
        self._breed=breed               #protected attribute
        self.__age=age                  #private attribute

    #public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"
    
    #Getter and Setter for private attribute
    def get_age(Self):
        return Self.__age
    
    #and Setter for private attribute
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")
    
obj1=Dogg("paw","german",21)
print(obj1.get_info())
print(obj1.name)  
#accessing protected member
print(obj1._breed) 
print(obj1.get_age())
obj1.set_age(11)
print(obj1.get_info())




#EXAMPLE 2
class BankAccount:

    def __init__(self,balance):
        self.__balance=balance #private attribute

    #getter method
    def get_balance(self):
        return self.__balance
        
    #setter method
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print(f"Successfully deposited {amount}")
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew {amount}")
        else:
            print(f"Invalid withdraw {amount}!")

myaccount = BankAccount(10000)
print(myaccount.get_balance()) #10000

myaccount.deposit(1000)
print(myaccount.get_balance())

myaccount.withdraw(2000)
print(myaccount.get_balance())
