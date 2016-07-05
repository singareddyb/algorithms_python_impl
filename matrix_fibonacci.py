#!/usr/bin/python
import sys
import pdb

'''
Fibonacci number generation in O(log n) for very small numbers

T(n) = T(n/2) + 1 -> O(log n)  for Fibonacci numbers that are very small

For Large Fibonacci number generation -- O(M(n)log (n)) where M(n) is the complexity of (multiplying and adding) very large numbers
'''

def matrix_fibonacci(n,matrix2):
  matrix1 = [[0,1],[1,1]]
  for i in range(1,n+1):
    matrix2 = multiply_matrices(matrix1, matrix2)
  return matrix2[0]

def multiply_matrices(matrix1, matrix2):
  matrix1_number_rows = len(matrix1)
  matrix2_number_rows = len(matrix2)
  assert(matrix1_number_rows == matrix2_number_rows)
  assert(matrix1_number_rows == 2)
  range_matrix2 = range(len(matrix2))

  ''' Need to make a deep-copy'''
  temp = list()
  for i in range_matrix2:
    temp.append(matrix2[i])

  ''' 4 multiplications and 2 additions
      Complexity matters for very large numbers - let it be M(n)
  '''
  for i in range_matrix2:
    e = 0
    for j in range_matrix2:
      e += matrix1[i][j]*temp[j] 
    matrix2[i] = e

  return matrix2

if __name__ == '__main__':
  input_num = sys.stdin.read()
  num = int(input_num)
  assert(num >= 0)
  F0 = 0
  F1 = 1
  if num == 0:
    fibonacci_number = F0
  elif num == 1:
    fibonacci_number = F1
  else:
    '''pdb.set_trace()'''
    fibonacci_number = matrix_fibonacci(num,[F0,F1])
  print(fibonacci_number)
