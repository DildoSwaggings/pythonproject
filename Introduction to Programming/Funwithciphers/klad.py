'''
Created on 24 jan. 2017

@author: tos340
'''
def square_sum(lst):
    for i in range(len(lst)):
        lst[i] = lst[i]**2
        print 'lijst kwadraat: %d' %lst[i]**2
    return sum(lst)
my_list = [1,2,3]
print(square_sum(my_list)) # Prints 14
print(square_sum(my_list))

lijst = range(0, 26)
print lijst