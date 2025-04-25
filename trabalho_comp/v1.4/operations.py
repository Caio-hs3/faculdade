from mathop import *
from utils import *

def get_matrix_to_operate(operation, data):
  '''Create a matrix to use in linear transformations. Their behavior depends on the current operation and input data.
    str, tuple -> list(tuple)'''
  if operation == 'cisalhamento':
    return [
        [1, data[0]], [data[1], 1]
    ]
  elif operation == 'rotacao':
    return [
        [math.cos(data[0]), -math.sin(data[0])], [math.sin(data[0]), math.cos(data[0])]
    ]
  elif operation == 'compressao':
    return [
        [data[0], 0], [0, data[1]]
    ]
  else:
    print('Operação invalida!')
    shutdown()

def transform_points(transformation_matrix, points):
  '''Apply matrix multiplication in a given matrix, in other words, this function transforms the points.
  list[list[float]], list[list[float]] -> list[list[float]]'''
  print(transformation_matrix, points)
  new_points = []
  for i in range(len(points)):
    new_points.append(product_between_two_matrices(transformation_matrix, points[i]))
  return new_points
