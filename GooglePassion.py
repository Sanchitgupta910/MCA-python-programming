# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:13:09 2021

@author: SANCHIT
"""

#creating a list for alphabets
ls=["g","o","l","e"," "," "," "," "]

#creating an  empty list to accept the input from the users
lst=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    e = int(input())
 
    lst.append(e) # adding the element into the list
    
str1="" #creating an empty string    
for i in lst:
    str1+=ls[i-1] #string concatenation
    if(i==8):
        str1=str1[::-1]#revsersing the string
    elif(i==7):
        str1=str1.capitalize()#capitalising string
    elif(i==6):#add . at the end of the string
        str1+='.'
    elif(i==5):
        str1=str1[:i-1]+str1[i-1].upper()+str1[i:]
       
print(str1)
                  