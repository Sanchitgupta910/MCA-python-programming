# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:01:53 2021

@author: SANCHIT

lab 8: Multilevel inheritence: to calculate the electricity bill

"""

class House:
    def house_name(self):        
        self.houseowner = input("Enter the name of the owner of the house: ")
        self.houseno = int(input("Enter the house no: "))     
    
        
        
class Bill(House):
    def calcbill(self):        
        self.meterno = int(input("Enter the meter no: "))
        self.units = float(input("Enter the no of units: "))
        self.rate_per_unit = float(input("Enter the rate per unit: "))
        self.bill = self.rate_per_unit * self.units
        
    

class Billdue(Bill):
    def duedate(self):
        self.duedate = int(input("Enter the due date of the month: "))
        self.paid = int(input("Enter the date you paid the bill: "))
        
            
class Printbill(Billdue):
    def printbilldetails(self):
        print("\nBilling name: ",self.houseowner)
        print("Billing address",self.houseno)
        print("Meter No: ",self.meterno)
        print("Bill Units: ",self.units)
        print("Bill amount: ", self.bill)
        if self.paid <= self.duedate:
            print("Bill paid successfully on time.")
        elif self.paid > self.duedate:
            print("Bill paid late! Pay the fine.")
    

b = Printbill()
b.house_name()
b.calcbill()
b.duedate()
b.printbilldetails()



            
         