'''
Created on 20 jan. 2017
Assigment 2. GeographyGrades3
@author: Thom
'''
#functions
from GeographyGrades1 import gemiddelde, cijfer_leerling
from GeographyGrades2 import bepaal_getal_achter_de_komma, bepaal_getal_voor_de_komma, rond_cijfer_af


def split_per_leerling(element_per_groep):
    for element in element_per_groep:
        element_per_leerling_met_groep = element.split('\n')
        element_per_leerling = element_per_leerling_met_groep[1:]
        groep = element_per_leerling_met_groep[0]
    return element_per_leerling, groep #dit is een lijst met twee elementen

if __name__ == "__main__": 
    
    file = open('datamodule4.txt')
    invoer = file.read()
    element_per_groep = invoer.split('\n=\n')
    for groep in element_per_groep:
        element_per_leerling = split_per_leerling(element_per_groep)[0]
        naam_groep = split_per_leerling(element_per_groep)[1]
    
    groepslijst = []
    for element in element_per_groep:
        groepslijst +=  element_per_groep[0]
       
    print 'Dit is de groepslijst: %s' %groepslijst 
    #element_per_leerling = element_per_groep.split('\n')
    
    
    for groeps_gegevens in element_per_groep:
        groep = bepaal_groep(groeps_gegevens)
        print 'Report for group %s'%(groep)
    
    for leerling in element_per_leerling:
        naam, cijfer = cijfer_leerling(leerling)
        afgerond_cijfer = rond_cijfer_af(cijfer)
        print '%s has a average grade of %.1f, so the rounded grade is: %.1f' %(naam, cijfer, afgerond_cijfer) 
            
    print 'End of report'
