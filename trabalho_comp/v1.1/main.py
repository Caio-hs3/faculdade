from plot import *
from mathop import *
from operations import *

def input_handler():
  '''Handles input from user to get essesntial information for the program
  None -> tuple, str'''
  quadrilatero = input('Insira as cordenadas do seu quadrilátero (exemplo: [[10, -2],[10,-4], [14, -2],[14, -4]]): ')
  operation = input('Insira a operação desejada (CISALHAMENTO; ROTACAO; COMPRESSAO): ')


def main():
  '''Main function of the code'''
  origin_matrix = [[10, -2],[10,-4], [14, -2],[14, -4]]
  x = degress_to_radians(76)
  transformation_matrix = get_matrix_to_operate('COMPRESSAO', [1, 1.4])
  points_after_transformation = transform_points(transformation_matrix, origin_matrix)
  print(points_after_transformation)
  show_polygon(origin_matrix, points_after_transformation, 'teste')

if __name__ == '__main__':
  main()