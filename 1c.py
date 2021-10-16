# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 20:26:19 2021

@author: SANCHIT

c.	DNAtoRNA: This script  takes in a DNA string and gives as output  RNA. Some information for your understanding is given below 
Given a DNA strand, return its RNA complement (per RNA transcription).
Both DNA and RNA strands are a sequence of nucleotides.
The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
•	G -> C
•	C -> G
•	T -> A
•	A -> U

"""

print("Enter any DNA sequence: ")
dna=input()
rna=dna.maketrans("ATGC", "UACG") #The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
print(dna.translate(rna))