'''
Created on 27 jan. 2017

@author: tos340
'''

file = open('inputnewton2.txt')
input = file.read()
input_split = input.split('\n')
algebraic_equation_from_file = input_split[0].split()
number_of_repetitions = int(input_split[1])
initial_guess_for_a_root = float(input_split[2])

print algebraic_equation_from_file

def read_function(algebraic_equation):
    #algebraic_equation_list = algebraic_equation.split()
    algebraic_equation_list = map(float, algebraic_equation)
    coefficients = algebraic_equation_list[0:-1:2]
    exponents = algebraic_equation_list[1::2]
    #print algebraic_equation_list
    #print coefficients
    #print exponents
    return coefficients, exponents, algebraic_equation_list

def derivative(algebraic_equation):
    coefficients, exponents, algebraic_equation_list = read_function(algebraic_equation)
    #coefficient_derivative_list = []
    algebraic_equation_derivative_list = []
    list_number_of_coefficients = range(0, len(coefficients))
    for number in list_number_of_coefficients:
        coefficient_float = float(coefficients[number])
        coefficient_derivative = coefficient_float * float(exponents[number])
        #coefficient_derivative_list.append(coefficient_derivative)
        algebraic_equation_derivative_list.append(coefficient_derivative)
        exponent_int = int(exponents[number])
        if exponent_int >= 1:
            exponent_derivative = exponent_int - 1
        elif exponent_int == 0:
            exponent_derivative = 0
        else: 
            print 'please give positive exponents only'
        algebraic_equation_derivative_list.append(exponent_derivative)
    return algebraic_equation_derivative_list


def function_value_at_x(algebraic_equation, x):
    coefficients, exponents, algebraic_equation_list = (read_function(algebraic_equation))
    sum = 0
    list_number_of_coefficients = range(0, len(coefficients))
    for number in list_number_of_coefficients:
        exponent_float = exponents[number] #float command can be removed?!?
        exponent_of_x = (x) ** (exponent_float)
        sum += (exponent_of_x * (coefficients[number]))
    return sum

def newton(algebraic_equation, number_of_repetitions, x_n):
    print 'dit is x_n: %f' %x_n
    if number_of_repetitions == 0:
        return x_n
    x_n_plus_1 = x_n - ((function_value_at_x(algebraic_equation, x_n))/  (function_value_at_x(derivative(algebraic_equation), x_n)))
    number_of_repetitions_new = number_of_repetitions - 1
    return newton(algebraic_equation, number_of_repetitions_new, x_n_plus_1)

print 'Newton test:' 

coefficient_read, exponent_read, algebraic_equation_read = read_function(algebraic_equation_from_file)   
uitkomst = newton(algebraic_equation_read, number_of_repetitions, initial_guess_for_a_root)
print 'This is your initial guess for the root: %f, this is your algebraic equation: %s, \
this is your number of repetitions: %s, this is your answer: %s.' %(initial_guess_for_a_root, \
algebraic_equation_from_file, number_of_repetitions, uitkomst)

    


#for repetition in range(int(number_of_repetitions)):
 #   x = 
    

