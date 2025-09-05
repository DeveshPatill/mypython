#constructor topic

class orders:
    def product_name():
        print("samosa")

    def product_price():
        print(800)

#objectname = class
customer = orders
customer.product_name()
customer.product_price()


print("----------------------------------------------------------------")
# important tips for constructors 
#1. constructor define kiya toh object ke sath class ko parenthesis dena padega
#2. constructor ko variable dena padega upar
#3. neeche waley functions ko bhi dena padega variable (AS AN BRIDGE TOH HI NEECHE WALE DOH FUNCTION CHALlENGE) 
class orders:
    def __init__(a):             
        print(18)
    def product_name(a):
        print("samosa")

    def product_price(a):
        print(800)

#objectname = class
customer = orders()
customer.product_name()
customer.product_price()

print("------------------------------------------------------------------")
# this is  Dynamic code
class creditcard:
    def __init__(self):
        print("bank hdfc")
        print("city name: Mumbai")

    def creditlimit(self,cl):
        self.cl = cl
        print(cl)
    def useamount(self,amount):
        mrp = self.cl-amount
        print(amount)
        print(mrp)


customer = creditcard()
customer.creditlimit(1000)
customer.useamount(500)

#------------------------------------------   inheritence ----------------------------------------------
#------------------------------------------ single inheritence -----------------------------------------

class bank:
    def bank_info():
        print("the bank name is : HDFC")
    def bank_address():
        print("borivali")

class customer(bank):
    def c_info():
        print("my name is rohan")

my_info=customer
my_info.bank_info()
my_info.bank_address()
my_info.c_info()


#multiple 
class employee():
    def emp_info():
        print("my name is devesh")
class job():
    def job_info():
        print("software devlopment")
class company(employee,job):
    def company_info():
        print("capegemini")


obj=company
obj.emp_info()
obj.job_info()
obj.company_info()




