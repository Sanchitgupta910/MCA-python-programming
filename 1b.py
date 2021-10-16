# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 20:10:16 2021

@author: SANCHIT

b.	Gerund - which gives output  
i.	A string prefixed with “to” if it is ending with “ing”
ii.	A string “Not a gerund” if does not end with “ing”
Example Gerund(“Painting”)-> to paint

"""

print("Input the srting") #taking input from the user
x=input()
if(x.endswith("ing")): #checking if the string ends with "ing" or not
    print("to " + x[:-3])
else:
    print("Not a gerund")
    