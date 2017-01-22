'''
Created on Jan 11, 2017

@author: thom
'''

#define constants
CALL_OUT_COSTS = float(16.00) #in eur

#input
hourly_wages = float((raw_input("Enter the hourly wages: "))) #in eur
hours_worked = float(raw_input("Enter the number of hours worked: "))

#calculate
round_hours_worked = round(hours_worked)
total_cost = float(hourly_wages * round_hours_worked + CALL_OUT_COSTS) #in eur

#output
print 'The total cost of this repair is: %.2f' %total_cost #in eur


