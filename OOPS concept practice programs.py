# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 21:09:08 2021

OOPS concept practice programs


@author: SANCHIT
"""

class Mobile:
    def apple(self):
        print("Hey Siri")
    def samsung(self):
        print("Hey Google")
    def price(self,price):
        self.price = price
    def color(self,color):
        self.color = color
    def show_color(self):
        print(self.color)
    def show_price(self):
        print(self.price)
    
        
    
    
mob= Mobile()
mob.apple()
mob.samsung() 
mob.color("Blue")
mob.price(50000)
mob.show_color()
mob.show_price()