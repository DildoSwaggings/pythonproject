'''
Created on 12 jan. 2017

@author: tos340
'''

#define constants
DISCOUNT_PERCENT = 15
PERCENT = 100

#input
price_first_article = float(raw_input('Enter the price of the first article: '))
price_second_article = float(raw_input('Enter the price of the second article: '))
price_third_article = float(raw_input('Enter the price of the third article: '))

#calculate

#determine most expensive article
if price_first_article > price_second_article and price_first_article > price_third_article:
    most_expensive_article = price_first_article
elif price_second_article > price_third_article:
    most_expensive_article = price_second_article
else:
    most_expensive_article = price_third_article
    
#determine discount
discount = (DISCOUNT_PERCENT * most_expensive_article ) / PERCENT 
total = price_first_article + price_second_article + price_third_article - discount

#output
print 'Discount: %.2f:' %discount
print 'Total: %.2f' %total