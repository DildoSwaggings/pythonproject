'''
Assigement: SecondSmallest
Created on 13 jan. 2017
@author: Thom Oosterhuis, tos340
'''

invoer = raw_input('Geef een aantal positieve gehele getallen en zorg ervoor \
dat het eerste getal kleiner dan het tweede getal is: ')
getallen_sequence = invoer.split()
#test: print invoer
#test: print getallen_sequence

getallen_integers = map(int, getallen_sequence)
#test print getallen_integers

kleinste_getal = getallen_integers[0]
# test: print kleinste_getal
een_na_kleinste_getal = getallen_integers[1]
#test: print een_na_kleinste_getal

for getal in getallen_integers:
    if getal < een_na_kleinste_getal and getal < kleinste_getal:
        een_na_kleinste_getal = kleinste_getal
        kleinste_getal = getal        
    elif getal < een_na_kleinste_getal:
        een_na_kleinste_getal = getal
        
print 'Het kleinste getal is %d.' %kleinste_getal
print 'Het een na kleinste getal is %d.'%een_na_kleinste_getal
