# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:48:32 2021

@author: SANCHIT
"""

def password():
    pw=input("Enter a password")
    if 6<=len(pw) and len(pw)<=19:
        if (any(pw.isdigit()) for char in pw):
            if (any(pw.isupper()) for char in pw):
                if (any(pw.islower()) for char in pw):
                    if (any())
    else:
        print("Weak password")

password()