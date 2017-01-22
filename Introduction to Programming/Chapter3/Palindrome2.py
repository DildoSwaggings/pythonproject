'''
Created on Jan 19 2017

@author: Thom
'''
#CONSTANTS
CENTERWIDTH = 51
#function

def generate_palindrome(n):
    getal_van_letter = ord(n) - ord('a')
    getallen = range(getal_van_letter)
    rij = ''
    for getal in getallen:
        getal2 =getal + ord('a')
        rij += chr(getal2)
    
    rij += n

    for getal in getallen:
        getal3 = getal_van_letter - getal + ord('a')-1
        rij += chr(getal3)
        
    print rij.center(CENTERWIDTH)
    
if __name__ == "__main__":
    #input
    letter = raw_input('Enter a letter: ')
 
    #execute
    generate_palindrome(letter)