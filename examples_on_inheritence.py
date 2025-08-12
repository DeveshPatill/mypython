##########################################single inheritence example
class electronics:
    def electricity():
        print("supplied electricity to devices")

    def on_off_switch():
        print("switch on")

class devices(electronics):
    def laptop():
        print("laptop ui started")

    def cellphone():
        print("switched on for calling")

    def printer():
        print("all ready printing") 

obj = devices
obj.electricity()
obj.on_off_switch()
obj.laptop()
obj.cellphone()
obj.printer()


################################# multipe inheritence example

class toyota_cars_types():
    def audi():
        pass
    def camry():
        pass
    def land_cruiser():
        print("1000000")
class mahindra_cars_types():   
    def mahindra_xuv():
        pass
    def mahindra_thar():
        pass
class audi_cars_types():
    def audi_q8():
        pass
    def audi_q6():
        pass
class car(toyota_cars_types,mahindra_cars_types,audi_cars_types):
    def vehicle():
        print("all cars are same")

obj=car
obj.audi()
obj.camry()
obj.land_cruiser()
obj.mahindra_xuv()
obj.mahindra_thar()
obj.audi_q6()
obj.audi_q8()
obj.vehicle()

#############################################heirarchial
class boss():
    def boss_info():

        print("name is : sukhdev")
        print("department : research organization")
        print("salary distribution between 2 employees 10000")

class employee_1(boss):
    def emp1_info():
        print("salary credited 10k")
class employee_2(boss):
    def emp1_info():
        print("salary credited 10k")

obj=employee_1
obj.boss_info()
obj.emp1_info()
obj.emp1_info()

################################## multilevel inehritence ##################################
        
class car_types:                         #parent
    def audi():
        print("my type audi2000000")
    
class audi(car_types):                   #child 1
    def audiz0000():
        print("mytype")

class audi_benz(audi,car_types):         #child 2
    def toyota():
        print("4000000000")

obj=audi_benz
obj.audi()
obj.audiz0000()
obj.toyota()




class bank:
    def __init__(self,existing_amount,tds):
        self.existing_amount = existing_amount
        self.tds=tds

    def add_amount(self,credit):
        self.credit=credit
        self.added_amount = credit + self.existing_amount
        print(f"amount credited {credit} in your account")

    def final_amount(self):
        tax_kata = self.added_amount*self.tds/100
        final_mrp = self.added_amount - tax_kata
        print(f"amount deducted from your acc,tds amount {tax_kata}")
        print(f"this is yours final mrp {final_mrp}")

obj = bank(50000,10)
obj.add_amount(50000)
obj.final_amount()



    

            








