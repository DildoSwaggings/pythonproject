'''
Created on 31 jan. 2017
Assigment Determinant
@author: Thom, tos340
'''
####READING FILE AND MATRICES IN FILE###
file = open('matrix1punt1.txt').read()
list_of_matrices_from_file = file.split('=\n')

###functions###
def read_matrix(list_of_matricses, number):
    result = []
    matrix = list_of_matricses[number]
    input = matrix.split('\n')
    for line in input:
        row = map(int, line.split())
        result.append(row)
    result = result[0:-1] ###This can be done in an nicer way
    return result

def print_matrix(matrix):
    for row in matrix:
        print row
        
def determinant_two_by_two_matrix(two_by_two_matrix):
    a, b, c, d = read_elements_two_by_two_matrix(two_by_two_matrix)
    determinant = (a * d) - (b * c)
    return determinant

def read_elements_two_by_two_matrix(two_by_two_matrix):
    row_one = two_by_two_matrix[0]
    row_two = two_by_two_matrix[1]
    a = row_one[0]
    b = row_one[1]
    c = row_two[0]
    d = row_two[1]
    return a, b, c, d

def check_and_give_lenght_matrix(n_by_n_matrix):
    number_of_rows = len(n_by_n_matrix)
    for row in n_by_n_matrix:
        if len(row) != number_of_rows:
            print 'The given matrix is not a square matrix, pleas check your input'
            return
    return number_of_rows

def delete_column(column_number, matrix):
    return ''
 
def determinant_n_by_n_matrix(n_by_n_matrix):
    lenght_matrix = check_and_give_lenght_matrix(n_by_n_matrix)
    if lenght_matrix == 2:
        return determinant_two_by_two_matrix(n_by_n_matrix)
    row_one = n_by_n_matrix[0]
    matrix_without_row_one = n_by_n_matrix[1, lenght_matrix]
    determinant = 0
    for number in range(lenght_matrix):
        determinant += row_one[number] * determinant_n_by_n_matrix(delete_column(number, matrix_without_row_one))
    return determinant

#VRAGEN OP WERKCOLLEGE
#inlezen zdd spaties aan einde bij input bestand wegvallen
#staat return in determinant_n_by_n_matrix() op goede plek??
#TESTING:
result = read_matrix(list_of_matrices_from_file, 0)
print result
print_matrix(result)
determinant = determinant_two_by_two(result)
print determinant
print read_elements_two_by_two_matrix(result)
print check_and_give_lenght_matrix(result)
#'''
