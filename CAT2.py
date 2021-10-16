# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:35:33 2021

@author: SANCHIT
"""

class intelligencer:
    def _init_(self,secret_code):
        self.secret_code = secret_code

    @staticmethod
    def decode(secret_code):
        words = secret_code.split()
        new_words = []
        priority_list = []
        sorted_word_list = []
        for word in words:
            temp_word = []
            priority = 0
            for letter in list(word):
                if letter.isalpha():
                    temp_word.append(letter)
                else:
                    priority = letter
            new_words.append("".join(temp_word))
            priority_list.append(priority)

        for x in range(1,len(new_words)+1):
            for index,priority in enumerate(priority_list):
                if int(priority)==x:
                    sorted_word_list.append(new_words[index])
        return " ".join(sorted_word_list)

secret_code = input("Enter your code")
try:
    secret_code = str(secret_code)
    print(intelligencer.decode(secret_code))
except:
    ("Enter a valid input!")