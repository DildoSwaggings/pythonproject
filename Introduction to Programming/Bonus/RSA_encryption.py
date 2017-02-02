'''
Created on 2 feb. 2017

@author: tos340
'''
FIRST_PRIME=2

def generate_primes(last_number):
    numbers = range(FIRST_PRIME,last_number)
    rounded_root_of_last_number = int((last_number**0.5)+1)
    multiplies = range(FIRST_PRIME, rounded_root_of_last_number)
    #print numbers
    for number in range(FIRST_PRIME,last_number):
        #for number2 in range(FIRST_PRIME, last_number/number):
            for multiply in multiplies:
                power_multiplied_by_multiply = number * multiply
                print power_multiplied_by_multiply
                if power_multiplied_by_multiply in numbers:
                    numbers.remove(power_multiplied_by_multiply)
    return numbers

def determine_decomposition_in_two_primes(n):
    list_of_primes = generate_primes(n+1)
    for prime1 in list_of_primes:
        for prime2 in list_of_primes:
            product = prime1 * prime2
            if product == n:
                return prime1, prime2
            
            


#'''
###testing
#print generate_primes(1001)
print determine_decomposition_in_two_primes(713)
###'''