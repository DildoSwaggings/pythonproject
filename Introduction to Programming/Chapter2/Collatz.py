'''
Assigment: Collatz
Created on 13 jan. 2017
@author: Thom Oosterhuis, tos340
'''
#assigment:
# if n is even, the next number is n/2
# is n is odd, the next number is 3n + 1

#input
integer = long(raw_input('Please enter a positive integer: '))
modulo = integer % 2
print integer,

while integer != 1 :
    if modulo == 1 :
        integer = 3 * integer +1
        modulo = integer % 2
        print integer,
    else:
        integer = integer / 2
        modulo = integer % 2
        print integer,


