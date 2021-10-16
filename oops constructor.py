# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 21:33:38 2021
OOPS USING CONSTRUCTOR

@author: SANCHIT
"""

class Car:
    def __init__(self,model,color,engine,price): #defining constructor using __init__
        self.model=model
        self.color=color
        self.engine=engine
        self.price=price
    
    def print_mercedez(self): #normal function toprint the values
        print("The Mercedez model no is: ", self.model)
        print("The Mercedez color is: ", self.color)
        print("The Mercedez engine is: ", self.engine)
        print("The Mercedez price is: ", self.price)
        

merz= Car("A135S", "black", "petrol", "$50M") #assigning values while creating the object using constructor
merz.print_mercedez()

