'''
Created on 19 jan. 2017

@author: tos340
'''

def gemiddelde(a):
    cijfers = a.split(' ')
    cijfer1 = float(cijfers[0])
    cijfer2 = float(cijfers[1])
    cijfer3 = float(cijfers[2])
    gemiddelde = (cijfer1 +cijfer2 + cijfer3)/3
    return gemiddelde

print gemiddelde('5 6.2 7')