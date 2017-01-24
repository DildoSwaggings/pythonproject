'''
Created on 24 jan. 2017
Assigment Introduction to binary numbers
@author: Thom
'''

def to_binary2(getal):
    if getal == 0:
        return ''
    else:
        return to_binary2(getal/2) + str(getal%2)

getal = to_binary2(0)
print getal

def to_decimal(bin):
    lijst = map(int, str(bin))
    print lijst
    som = 0
    teller = 0
    for element in lijst:
        som += element * 2**(int(len(lijst))-teller-1)
        teller += 1                    
    print som
    
to_decimal(101010)