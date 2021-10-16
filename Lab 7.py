# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:45:08 2021

@author: SANCHIT

LAB 7  CLASSES AND OBJECTS   

"""

#creating a class vehicle
class Vehicle:
    
    #defining constructor using __init__ and pass self is mandatory in OOP
    def __init__ (self, brand, model, vehicle_type, fuel_tank_size, fuel_level):
        
        #creating instance variable
        self.brand = brand     
        self.model = model
        self.vehicle_type = vehicle_type
        self.fuel_tank_size = fuel_tank_size
        self.fuel_level = fuel_level
    
    #definig a funcn to check the fuel level
    def Fulltank(self):        
        if self.fuel_level==self.fuel_tank_size:
            print("Tank is full")
        elif self.fuel_level<self.fuel_level:
            print("Tank is not full")
        
    #defining a funcn to enter the new fuel level
    def Update_fuel_tank(self):
        self.new_level =int(input("Enter the new fuel level: "))
        self.new_level = self.new_level + self.fuel_level
        if self.new_level <= self.fuel_level:
            print("Low Fuel!!")   
        elif self.new_level > self.fuel_level:
            print("Good to go :)")
            
    #desining a funcn to take to input of fuel amount        
    def Get_fuel(self):
        self.amount = int(input("Enter the amount of fuel: "))
        self.amount = self.amount + self.new_level
        if self.amount >= self.fuel_tank_size:
            print("Tank Full!!")
        elif self.amount < self.fuel_tank_size:
            print("ThankYou!")
    def Drive(self):
        print("Wow! I am driving", self.model)
        
#creating two objects of the class vehicle        
            
merz= Vehicle("Mercedez", "Mercedez A551S", "Petrol", 10, 5)
hyun = Vehicle("Hyundai", "Hyundai Tornnado", "Diesel", 15, 3)

#calling the funcn using the object      
merz.Fulltank()
merz.Update_fuel_tank()
merz.Get_fuel()
merz.Drive()

hyun.Fulltank()
hyun.Update_fuel_tank()
hyun.Get_fuel()
hyun.Drive() 
                                
        