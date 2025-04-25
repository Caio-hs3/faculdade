import ast
import sys

def string_to_matrix(input):
  '''Transform input matrix in string format to python'''
  input_ = input.strip()
  matrix = ast.literal_eval(input_)
  
  return matrix

def shutdown():
  '''Function to be called when the user inputs '0' in any of the input fields with teh intention of exiting the program'''
  print('Até a próxima!')
  sys.exit(0)