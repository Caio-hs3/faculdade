from plot import *
from mathop import *
from operations import *

def main():
'''main function of the code'''
  origin_matrix = [[10, -2],[10,-4], [14, -2],[14, -4]]
  x = degress_to_radians(76)
  transformation_matrix = get_matrix_to_operate('COMPRESSAO', [1, 1.4])
  dots_after_transformation = transform_dots(transformation_matrix, origin_matrix)
  print(dots_after_transformation)
  show_polygon(origin_matrix, dots_after_transformation, 'teste')

if __name__ == '__main__':
  main()