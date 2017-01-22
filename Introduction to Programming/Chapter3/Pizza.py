'''
Created on 19 jan. 2017
Assigment 5. Pizza
@author: Thom
'''

#CONSTANTS
TOTAL_INGREDIENTS_MARIO = 10
TOTAL_INGREDIENTS_LUIGI = 9
INGREDIENTS_PER_PIZZA_MARIO = 3
INGREDIENTS_PER_PIZZA_LUIGI = 4

#functions:
def faculteit(n):
    getallen = range(1, n+1)
    uitkomst = 1
    for getal in getallen:
        uitkomst *= getal
        
    return uitkomst

def n_boven_k(n, k):
    n_faculteit = faculteit(n)
    k_faculteit = faculteit(k)
    m = (n - k)
    n_min_k_faculteit = faculteit(m)
    uitkomst = n_faculteit / ((k_faculteit)*(n_min_k_faculteit))
    return uitkomst

#calculate
aantal_pizzas_mario = n_boven_k(TOTAL_INGREDIENTS_MARIO, INGREDIENTS_PER_PIZZA_MARIO)
aantal_pizzas_luigi = n_boven_k(TOTAL_INGREDIENTS_LUIGI, INGREDIENTS_PER_PIZZA_LUIGI)

#print
print 'Mario can make %d pizzas' %aantal_pizzas_mario
print 'Luigi can make %d pizzas' %aantal_pizzas_luigi

if aantal_pizzas_mario > aantal_pizzas_luigi:
    print 'Mario has won the bet.' 
elif aantal_pizzas_luigi > aantal_pizzas_mario:
    print 'Luigi has won the bet.'
else:
    print 'ERROR'
    
    
         