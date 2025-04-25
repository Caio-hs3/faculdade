
from mathop import *

def get_matrix_to_operate(operation, data):
  '''Create a matrix to use in linear transformations. Their behave depends on the operation and the data.
    str, tuple --> list(tuple)'''
  if operation == 'CISALHAMENTO':
    return [
        [1, data[0]], [data[1], 1]
    ]
  if operation == 'ROTACAO':
    return [
        [math.cos(data[0]), -math.sin(data[0])], [math.sin(data[0]), math.cos(data[0])]
    ]
  if operation == 'COMPRESSAO':
    return [
        [data[0], 0], [0, data[1]]
    ]

def transform_dots(transformation_matrix, dots):
  '''Apply matrix multiplication in some matrices, in other words, this function transformate the dots.
  list[list[float]], list[list[float]] -> list[list[float]]'''
  new_dots = []
  for i in range(len(dots)):
    new_dots.append(product_between_two_matrices(transformation_matrix, dots[i]))
  return new_dots