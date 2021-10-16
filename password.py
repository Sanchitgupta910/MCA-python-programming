# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:40:12 2021

@author: SANCHIT
"""

# Lambda function to check if a given vaue is from 10 to 20.
import random


test = lambda x : False and print("weak password") if((len(x) < 8 or len(x) > 20) or not any(char.isdigit() for char in x) or not any(char.isupper() for char in x or not any(char.islower() for char in x) or not any(char in ['$', '@', '#', '%','!','*','^'] for char in x)) ) else print("Secure Password! ") 
# Check if given numbers are in range using lambda function
x=input("Enter the Password")
if test(x)==False:

  lowercase = "abcdefghijklmnopqrstuvwxyz"
  uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "0123456789"
  symbols = "[]{}()*;/.,-_"

  all = lowercase + uppercase + numbers + symbols
  length = int(input("------------- WEAK PASSWORD ------------\n\nEnter the length of new password")) 
  while 1:
     if length>7 :
        break;
     else :
       print("ENTER LENGTH GREATER THAN 8")
       length = int(input("Enter the length")) 
    #Change this number to change the length of your password

  password = "".join(random.sample(all,length)) #creating a random password using the funcn random()
  print("Suggested Password {}".format(password))
  print("PRESS 1 TO USE THE SAME PASSWORD \n 2 to ENTER NEW PASSWORD")
  choose=int(input())
  if choose==1:
     
     test(password)
     print("YOUR PASSWORD {}".format(password))
  else :
     print("---------Enter new Password----------")
     x=input()
     test(x)
     while(test(x)==False):
        x=input("-------WEAK PASSWORD----------")
        test(x)