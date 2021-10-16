''' a python script a.	AppleOrangeBannana  : which gives output  
i.	string “Apple” if the input is string
ii.	string “Orange” if the input is number
iii.	string “Bannana” for anything else

Author Sanchit Gupta
Date: 23Aug'21 '''

fruits='AppleOrangeBannana' 
print('enter anything: ') #taking input from the user
x=input()
if (x.isalpha()): # checking the input is alphabet or not
    print (fruits[0:5])
elif(x.isdigit()): # checking the input is integer or not
    print(fruits[5:11]) 
else:
    print(fruits[11:])
