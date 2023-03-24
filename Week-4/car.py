#!/usr/bin/env/python3
#python programs on oop
#Name : Anita Sofia 
#Email : anitasofia254@gmail.com
#Date : 27th Feb 2023
#File : car.py

class car:
    def __init__(self,model,make,year,engine_capacity):
        self.model = model
        self.make = make
        self.year = year_of_man
        self.engine_capacity = engine_capacity
    
#getters
    def get_model(self):
        return self.model
        
    def get_make(self):
        return self.make

    def get_year(self):
        return self.year

    def get_engine_capacity(self):
        return self.engine_capacity

#setters
    def set_model(self,model):
        self.model = model

    def set_make(self):
        self.make = make

    def set_year_of_man(self):
        self.year_of_man = year_of_man

    def set_engine_capacity(self):
        self.engine_capacity = engine_capacity
        

car1 = car("demio","mazda","2019",1300)
car2 = car("deluxe","toyota","2020",3500)
car3 = car("passat","vw","2009",2600)

car3.set_year(2023)
car1.set_year(2026)
car1.set_model("tuareg")

print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car2.get_year())

print(car3.get_model())
print(car3.get_year())