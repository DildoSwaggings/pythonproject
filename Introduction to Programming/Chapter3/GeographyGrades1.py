'''
Created on 20 jan. 2017
Assigment 6. Geography Grades 1
@author: Thom
'''

#constants
AANTAL_TOETSEN = 3
LAAGST_MOGELIJKE_CIJFER = 1.0
HOOGST_MOGELIJKE_CIJFER = 10.0

#functions

def gemiddelde(losse_cijfers):
    som = 0
    for cijfer in losse_cijfers:
        som += cijfer
    gemiddelde = som / len(losse_cijfers)
    return gemiddelde
    

def cijfer_leerling(leerling):
    lijst_per_leerling = leerling.split('_')
    naam = lijst_per_leerling[0]
    cijfers = lijst_per_leerling[-1]
    cijfers_gestript = cijfers.split()
    losse_cijfers = map(float, cijfers_gestript)
    gemiddelde_cijfer = gemiddelde(controleer_aantal_cijfers(losse_cijfers))
    return naam, gemiddelde_cijfer, losse_cijfers

def controleer_range_cijfers(losse_cijfers):
    controle = 0
    for los_cijfer in losse_cijfers:
        if los_cijfer >= LAAGST_MOGELIJKE_CIJFER and los_cijfer <= HOOGST_MOGELIJKE_CIJFER:
            controle = controle
        else:
            controle += 1
    return controle

#controleert aantal cijfers en vult aantal cijfers aan met LAAGS_MOGELIJKE_CIJFER tot AANTAL_TOETSEN        
def controleer_aantal_cijfers(losse_cijfers):
    while len(losse_cijfers) < AANTAL_TOETSEN:
        losse_cijfers.append(LAAGST_MOGELIJKE_CIJFER)
    return losse_cijfers

#execute
    
if __name__ == "__main__": 
    #input
    file = open('data_module3.txt')
    invoer = file.read()
    element_per_leerling = invoer.split('\n')
    
    #control input and execute, else return error
    #output
    print 'Report for group 2b'
    
    for leerling in element_per_leerling:
        naam, gemiddelde_cijfer, losse_cijfers = cijfer_leerling(leerling)
        controle_range_cijfers = controleer_range_cijfers(losse_cijfers)
        if controle_range_cijfers != 0:
            print 'There is an error in the range of the grades of %s'%naam
        else:    
            print '%s has a average grade of %.1f' %(naam, gemiddelde_cijfer)
       
    print 'End of report'
 
    