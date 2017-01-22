'''
Created on 20 jan. 2017

@author: tos340
'''
#functions
from GeographyGrades1 import gemiddelde, cijfer_leerling
from GeographyGrades2 import bepaal_getal_achter_de_komma, bepaal_getal_voor_de_komma, rond_cijfer_af

def bepaal_groep(element):
    lijst = element.split('\n')
    groep = lijst[0]
    return groep
    
def bepaal_leerling(element):
    lijst = element.split('\n')
    element_per_leerling = lijst [1::]
    return element_per_leerling

if __name__ == "__main__": 
    
    file = open('datamodule4.txt')
    invoer = file.read()
    element_per_groep = invoer.split('\n=\n')
    
    for element in element_per_groep:
        groepsnaam = bepaal_groep(element)
        print 'Report for group %s' %groepsnaam
        element_per_leerling = bepaal_leerling(element)
        for leerling in element_per_leerling:
            naam, cijfer = cijfer_leerling(leerling)
            afgerond_cijfer = rond_cijfer_af(cijfer)
            print '%s has a average grade of %.1f, so the rounded grade is: %.1f' %(naam, cijfer, afgerond_cijfer)
        print 'End of report \n'    
        
    