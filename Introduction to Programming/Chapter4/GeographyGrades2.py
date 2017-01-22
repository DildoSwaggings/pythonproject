'''
Created on 20 jan. 2017

@author: tos340
'''
#functions
from GeographyGrades1 import gemiddelde, cijfer_leerling

def bepaal_getal_achter_de_komma(a):
    a = str(a)
    split1 = a.split('.')
    getal_achter_de_komma = split1[1]
    return float(getal_achter_de_komma)

def bepaal_getal_voor_de_komma(a):
    a = str(a)
    split1 = a.split('.')
    getal_voor_de_komma = split1[0]
    return float(getal_voor_de_komma)

def rond_cijfer_af(a):
    getal_voor_de_komma = bepaal_getal_voor_de_komma(a)
    getal_achter_de_komma = bepaal_getal_achter_de_komma(a)
    if getal_achter_de_komma == '3' or getal_achter_de_komma == '4' or \
    getal_achter_de_komma =='5' or getal_achter_de_komma == '6' or \
    getal_achter_de_komma == '7':
        afgerond_cijfer = getal_voor_de_komma + 0.5
    else:
        afgerond_cijfer = round(a)
    if afgerond_cijfer == 5.5:
        afgerond_cijfer == 6.0
    return afgerond_cijfer

if __name__ == "__main__": 
    #input
    file = open('data_module3.txt')
    invoer = file.read()
    element_per_leerling = invoer.split('\n')
    
    #output
    print 'Report for group 2b'
    
    for leerling in element_per_leerling:
        naam, cijfer = cijfer_leerling(leerling)
        afgerond_cijfer = rond_cijfer_af(cijfer)
        print '%s has a average grade of %.1f, so the rounded grade is: %.1f' %(naam, cijfer, afgerond_cijfer) 
            
    print 'End of report'