# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:08:21 2021

@author: SANCHIT
"""
#creating 2 empty lists
list = []
list1 = []
n = int(input("Enter number of words entering : "))

# iterating till the range
for i in range(0, n):
    ele = input()
    list.append(ele)  # adding the element
print(list)

for i in list:
    for j in i:
        if j not in list1:
                list1.append(j)
convertList = ''.join(map(str,list1))
print(f'Final List is ={convertList.split()}')