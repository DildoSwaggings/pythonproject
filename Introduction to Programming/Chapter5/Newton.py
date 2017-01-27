'''
Created on 27 jan. 2017

@author: tos340
'''

file = open('inputnewton1.txt')
input = file.read()
input_split = input.split('\n')
algebraic_equation = input_split[0]
number_of_repetitions = int(input_split[1])
initial_guess_for_a_root = float(input_split[2])

print algebraic_equation

def read_function(algebraic_equation):
    algebraic_equation_list = algebraic_equation.split()
    coefficients = algebraic_equation_list[0:-1:2]
    exponents = algebraic_equation_list[1::2]
    print algebraic_equation_list
    print coefficients
    print exponents
    return coefficients, exponents

read_function(algebraic_equation)

def derivative(algebraic_equation):
    coefficients, exponents = read_function(algebraic_equation)
    coefficient_derivative_list = []
    for coefficient in coefficients:
        coefficient_float = float(coefficient)
        coefficient_derivative = coefficient_float * float(exponents[coefficients.index(coefficient)])
        coefficient_derivative_list.append(coefficient_derivative)
    exponent_derivative_list = []
    for exponent in exponents:
        exponent_int = int(exponent)
        if exponent_int >= 1:
            exponent_derivative = exponent_int - 1
        elif exponent_int == 0:
            exponent_derivative = 0
        else: 
            print 'please give positive exponents only'
        exponent_derivative_list.append(exponent_derivative)
    print coefficient_derivative_list
    print exponent_derivative_list
        
derivative(algebraic_equation)

def function_value_at_x(algebraic_equiation, x):
    coefficients, exponents = (read_function(algebraic_equation))
    sum = 0
    for exponent in exponents:
        exponent_float = float(exponent)
        exponent_of_x = x * (exponent_float)
        sum += exponent_of_x * float(coefficients[exponents.index(exponent)])
    return sum

def newton(algebraic_equation, number_of_repetitions, x_n):
    if number_of_repetitions == 0:
        return x_n
    x_n_plus_1 = x_n * ((function_value_at_x(algebraic_equation, x_n))/  (function_value_at_x(derivative(algebraic_equation), x_n)))
    newton(algebraic_equation, (number_of_repetitions - 1), x_n_plus_1)
    
uitkomst = newton(algebraic_equation, number_of_repetitions, initial_guess_for_a_root)
print uitkomst
    
                        


#for repetition in range(int(number_of_repetitions)):
 #   x = 
    

