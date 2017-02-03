'''
Created on 27 jan. 2017
Module 5, Assignment Newton
@author: Thom, tos340
'''

###functions###
def read_function(algebraic_equation):
    algebraic_equation_list = map(float, algebraic_equation)
    coefficients = algebraic_equation_list[0:-1:2]
    exponents = algebraic_equation_list[1::2]
    return coefficients, exponents

def derivative(algebraic_equation):
    coefficients, exponents = read_function(algebraic_equation)
    algebraic_equation_derivative_list = []
    list_number_of_coefficients = range(0, len(coefficients))
    for number in list_number_of_coefficients:
        coefficient_float = float(coefficients[number])
        coefficient_derivative = coefficient_float * float(exponents[number])
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
    coefficients, exponents = (read_function(algebraic_equation))
    sum = 0
    list_number_of_coefficients = range(0, len(coefficients))
    for number in list_number_of_coefficients:
        exponent_float = float(exponents[number])
        exponent_of_x = (x) ** (exponent_float)
        sum += (exponent_of_x * (coefficients[number]))
    return sum

def newton(algebraic_equation, number_of_repetitions, x_n):
    if number_of_repetitions == 0:
        return x_n
    x_n_plus_1 = x_n - ((function_value_at_x(algebraic_equation, x_n))/  (function_value_at_x(derivative(algebraic_equation), x_n)))
    number_of_repetitions_new = number_of_repetitions - 1
    return newton(algebraic_equation, number_of_repetitions_new, x_n_plus_1)

def read_file_and_start(filename):
    file = open(filename)
    input = file.read()
    input_split = input.split('\n')
    algebraic_equation_from_file = input_split[0].split()
    number_of_repetitions = int(input_split[1])
    initial_guess_for_a_root = float(input_split[2])
    #
    uitkomst = newton(algebraic_equation_from_file, number_of_repetitions, initial_guess_for_a_root)
    print 'This is your initial guess for the root: %.2f, this is your algebraic equation: %s,\
    this is your number of repetitions: %s, this is your answer: %.1f.' %(initial_guess_for_a_root, \
    algebraic_equation_from_file, number_of_repetitions, uitkomst)
    
    
###execute###
if __name__ == '__main__':
    read_file_and_start('inputnewton2.txt')
    
    
    

    

