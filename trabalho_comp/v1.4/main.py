from plot import *
from mathop import *
from operations import *
from user import *

def main():
  origin_matrix, operation, operationData = input_handler()
  transformation_matrix = get_matrix_to_operate(operation, operationData)
  points_after_transformation = transform_points(transformation_matrix, origin_matrix)
  print(points_after_transformation)
  show_polygon(origin_matrix, points_after_transformation, 'teste')

if __name__ == '__main__':
  main()