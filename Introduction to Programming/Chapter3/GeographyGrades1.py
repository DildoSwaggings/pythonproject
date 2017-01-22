'''
Created on 20 jan. 2017
Assigment 6. Geography Grades 1
@author: Thom
'''

#constants
AANTAL_TOETSEN = 3

#functions
'''def controleer_cijfers(cijfers):
    gecontroleerde_cijfer_lijst = []
    for cijfer in cijfers:
        #if cijfer >= 1.0 and cijfer <= 10.0:
        gecontroleerde_cijfer_lijst =  gecontroleerde_cijfer_lijst(-1, cijfer)
    return gecontroleerde_cijfer_lijst
'''
def gemiddelde(a):
    cijfers = map(float, a.split(' '))#map
    som = 0
    for cijfer in cijfers:
        som += cijfer
    gemiddelde = som / len(cijfers)
    return gemiddelde
    

def cijfer_leerling(leerling):
    lijst_per_leerling = leerling.split('_')
    naam = lijst_per_leerling[0]
    cijfer = gemiddelde(lijst_per_leerling[-1])
    return naam, cijfer

def controleer_range_cijfers(leerling):
    lijst_per_leerling = leerling.split('_')
    cijfers = lijst_per_leerling[-1]
    losse_cijfers = map(float, cijfers.split(' '))
    controle = 0
    for los_cijfer in losse_cijfers:
        if los_cijfer >= 1.0 and los_cijfer <= 10.0:
            controle = controle
        else:
            controle += 1
    return controle
        
def controleer_aantal_cijfers(leerling):
    lijst_per_leerling = leerling.split('_')
    cijfers = lijst_per_leerling[-1]
    losse_cijfers = map(float, cijfers.split(' '))
    controle = 0
    if len(losse_cijfers) == AANTAL_TOETSEN:
        controle = controle
    else:
        controle += 1
    return controle
    
if __name__ == "__main__": 
    #input
    file = open('data_module3.txt')
    invoer = file.read()
    element_per_leerling = invoer.split('\n')
    
    #control input and execute, else return error
     
    #output
    print 'Report for group 2b'
    
    for leerling in element_per_leerling:
        naam, cijfer = cijfer_leerling(leerling)
        controle_range_cijfers = controleer_range_cijfers(leerling)
        controle_aantal_cijfers = controleer_aantal_cijfers(leerling)
        if controle_range_cijfers != 0:
            print 'There is an error in the range of the grades of %s'%naam
        else:
            if controle_aantal_cijfers != 0:
                print 'There is an error in the number of grades of %s'%naam
            else:      
                print '%s has a average grade of %.1f' %(naam, cijfer)
       
        
    print 'End of report'
 
    