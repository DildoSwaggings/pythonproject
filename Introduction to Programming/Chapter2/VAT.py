'''
Created on Jan 10, 2017

@author: thom
'''

#define constants
VAT=21 #VAT in percent
PERCENT=100
 
#code input
price_with_vat = float(raw_input("Please enter the price of an article including VAT in USD: $")) #price is in USD

#calculate price without vat in 
price_without_vat = (price_with_vat / (PERCENT + VAT)) * PERCENT

print 'The price of the article without VAT is $%.2f' %price_without_vat
#print 'This article will cost %.2f without %d VAT.' %(price_without_vat, VAT)