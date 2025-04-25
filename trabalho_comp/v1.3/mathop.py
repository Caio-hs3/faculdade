import math
'''This module contains the mathematical operations used in the rest of the project'''

def product_between_two_matrices(transformation_matrix, points_matrix):
  '''Create new matrices created by the product of two other matrices
  list[list[float]], list[list[float]] -> list[float]'''
  new_matrix = []
  final_value = 0
  for i in range(len(transformation_matrix)):
    for j in range(len(transformation_matrix[i])):
      final_value += (transformation_matrix[i][j] * points_matrix[j])
    new_matrix.append(final_value)
    final_value = 0
  return new_matrix

def degress_to_radians(degrees):
  '''Convert degrees to radians
  float -> float'''
  return (degrees * math.pi) / 180
