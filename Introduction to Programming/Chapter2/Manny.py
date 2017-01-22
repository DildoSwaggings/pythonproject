'''
Created on 12 jan. 2017

@author: tos340
'''
#constants
MINIMUM_DONATION = 50
#input
amount_of_donation = float(raw_input('Enter the amount you want to donate: '))

#output
while amount_of_donation < MINIMUM_DONATION:
    amount_of_donation = float(raw_input('Enter the amount you want to donate: '))
    
    
print 'Thank you very much for your contribution of %.2f euro' %amount_of_donation


