'''
Created on 31 jan. 2017
Assigment Determinant
@author: Thom, tos340
'''

###functions###
def read_matrix(list_of_matricses, number):
    result = []
    matrix = list_of_matricses[number]
    input = matrix.splitlines()
    for line in input:
        row = map(int, line.split())
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print element,
        print '' #This makes a new line for a new row

def check_and_give_lenght_n_by_n_matrix(n_by_n_matrix):
    number_of_rows = len(n_by_n_matrix)
    for row in n_by_n_matrix:
        if len(row) != number_of_rows:
            print 'The given matrix is not a square matrix, pleas check your input'
            return
    return number_of_rows

def give_matrix_with_deleted_column(column_number, matrix):
    new_matrix = [row[0:column_number] + row[column_number + 1:] for row in matrix]
    return new_matrix
 
def determinant_n_by_n_matrix(n_by_n_matrix):
    lenght_matrix = check_and_give_lenght_n_by_n_matrix(n_by_n_matrix)
    if lenght_matrix == 1:
        return int(n_by_n_matrix[0][0])
    row_one = n_by_n_matrix[0]
    matrix_without_row_one = n_by_n_matrix[1: lenght_matrix]
    determinant = 0
    for number in range(len(row_one)):
        determinant += (-1)**(number) * row_one[number] * determinant_n_by_n_matrix(give_matrix_with_deleted_column(number, matrix_without_row_one))
    return determinant

def read_file_and_start(filename, number_of_matrix_in_file):
    file = open(filename).read()
    list_of_matrices_from_file = file.split('=\n')
    matrix_from_file = read_matrix(list_of_matrices_from_file, number_of_matrix_in_file)
    determinant = determinant_n_by_n_matrix(matrix_from_file)
    print 'The determinant of the matrix '
    print_matrix(matrix_from_file)
    print 'is \n%.2f'%(determinant)
    
     
###execute###
if __name__ == '__main__':
    read_file_and_start('matrix3.txt', 1)

