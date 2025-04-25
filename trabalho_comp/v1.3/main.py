from plot import *
from mathop import *
from operations import *

def input_handler():
  '''Handles input from user to get essesntial information for the program
  None -> tuple, str, tuple/float'''
  quadrilatero = list(input('Insira as cordenadas do seu quadrilátero (exemplo: [[10, -2],[10,-4], [14, -2],[14, -4]]): '))
  operation = input('Insira a operação desejada (cisalhamento; rotacao; compressao): ').lower()
  # Initialize variables for later
  validOps = ['cisalhamento', 'rotacao', 'compressao']
  operationData = 0
  while operation not in validOps:
    operation = input('Operação invalida, por favor insira a operação desejada (cisalhamento; rotacao; compressao): ').lower()
  # Requests relevant information based on the type of operation the user wants
  if operation == 'rotacao':
    anguloRotacao = input('Insira o ângulo de rotação desejado (em graus): ')
    anguloRotacao = float(anguloRotacao)
    anguloRotacao = degress_to_radians(anguloRotacao)
    operationData == anguloRotacao
    if anguloRotacao == 0:
      print('Ângulo de rotação não pode ser 0. Fechando o programa.')
      shutdown()
    
  if operation == 'cisalhamento':
    cisX = input('Insira o fator de cisalhamento na direção x: ')
    cisY = input('Insira o fator de cisalhamento na direção y: ')
    cisX, cisY = float(cisX), float(cisY)
    operationData == [cisX, cisY]
    if cisX == 0 and cisY == 0:
      print('Ambos os fatores não podem ser iguais a 0 simultâneamente. Fechando o programa.')
      shutdown()

  if operation == 'compressao':
    escalaX = input('Insira o fator de escala na direção x: ')
    escalaY = input('Insira o fator de escala na direção y: ')
    escalaX, escalaY = float(escalaX), float(escalaY)
    operationData == [escalaX, escalaY]
    if escalaX == 1 and escalaY == 1:
      print('Ambos os fatores não podem ser iguais a 1 simultâneamente. Fechando o programa.')
      shutdown()

  return quadrilatero, operation, operationData

#def main():
  '''Main function of the code'''
  origin_matrix = [[10, -2],[10,-4], [14, -2],[14, -4]]
  x = degress_to_radians(76)
  transformation_matrix = get_matrix_to_operate('compressao', [1, 1.4])
  points_after_transformation = transform_points(transformation_matrix, origin_matrix)
  print(points_after_transformation)
  show_polygon(origin_matrix, points_after_transformation, 'teste')

origin_matrix, operation, operationData = input_handler()
print(operationData)
transformation_matrix = get_matrix_to_operate(operation, operationData)
def main():
 points_after_transformation = transform_points(transformation_matrix, origin_matrix)
 print(points_after_transformation)
 show_polygon(origin_matrix, points_after_transformation, 'teste')

if __name__ == '__main__':
  main()