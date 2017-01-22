'''
Created on 13 jan. 2017

@author: tos340
'''



def generate_palindrome():
    getallen = range(25)
    rij = ''
    for getal in getallen:
        getal2 =getal + 97
        rij += chr(getal2)
    
    rij += 'z'

    for getal in getallen:
        getal3 =24 - getal + 97
        rij += chr(getal3)
        
    print rij
 
generate_palindrome()
'''
sequence = 
for getal in getallen:
    getal2 = getal + 97
    sequence = sequence + chr(getal2),
    
print sequence
'''