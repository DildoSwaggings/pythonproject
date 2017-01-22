'''
Created on 19 jan. 2017

@author: tos340
'''
from Palindrome2 import generate_palindrome

getallen = range(ord('a'),ord('o'))

for getal in getallen:
    letter = chr(getal)
    generate_palindrome(letter)
    