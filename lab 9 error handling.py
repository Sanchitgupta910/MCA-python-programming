# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:06:45 2021

@author: SANCHIT

Lab 9: Error Handling
"""
#importing date time module for validating date
import datetime
inputDate = input("Enter your birth date (dd/mm/yy): ")

isValidDate = True
try:
    #splitting the date with /
    day, month, year = inputDate.split('/')
    
    #checking the validation of date
    datetime.datetime(int(year), int(month), int(day))
except ValueError:
    isValidDate = False


if(isValidDate):
    print("________________________________________________________________")
    if int(month) == 1:
        print("\ncapricon: Capricorns have an emotional side they keep hidden from everyone else - this is represented by the sea goat's hidden fish tail.")
    elif int(month) == 2:
        print("\nAquarius: The Aquarian's innate aptitude for understanding the energy around them.")
    elif int(month) == 3:
        print("\nPisces: Those who fall under the Pisces sign feel connected to others in the vast sea of the universe.")
    elif int(month) == 4:
        print("\nAries: Famously passionate, fiery and argumentative, it's no wonder Aries is symbolised by ram.")
    elif int(month) == 5:
        print("\nTaurus: Grounded in hard work, slow and steady perseverance and security, the bull is the persistent provider of the zodiac.   ")
    elif int(month) == 6:
        print("\nGemini: Geminis can be intelligent, adaptable an charming while also possessing nervous and indecisive traits.")
    elif int(month) == 7:
        print("\nCancer: Cancerians don't let go of things easily once they have crabbed on to something like ideas, goals and relationships.")
    elif int(month) == 8:
        print("\nLeo: Passionate, enthusiastic and ambitious, it's no wonder Leos are represented by a lion.")
    elif int(month) == 9:
        print("\nVirgo: A Virgo star sign is associated with organisation, good communication and high intelligence.")
    elif int(month) == 10:
        print("\nLibra: Charming, charismatic and easy to get on with, Libras love to find a balance in all areas of life.")
    elif int(month) == 11:
        print("\nScorpio: Known for their passion, persistence and hot-headed nature, a scorpion in an apt representation for a Scorpio.")
    elif int(month) == 12:
        print("\nSagittarius: They are also known to have high-reaching ideals and often shoot for the moon in terms of trying to live their life in an idealistic fashion.")
    
else:
    print("_____________________________________________________________")
    if inputDate == '?':
        print("\nEnter your Birthday in the given date format to know your Zodiac Sign!")
    elif inputDate == 'q' or inputDate =='Q':
        print("\nBye! Hope you run this program again.")
    elif inputDate == '':
        print("\nMy Zodiac sign is VIRGO: A Virgo star sign is associated with organisation, good communication and high intelligence.")
    else:
        print("\nEnter a valid date.")
    

