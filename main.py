#!/usr/bin/env python3

class SparseMatrix:
  def __init__(self, numRows=0, numCols=0):
    self.matrix = {}
    self.numRows = numRows
    self.numCols = numCols
    
  @staticmethod
  def load(matrixFilePath=None):
    if not matrixFilePath:
      return None
    
    try:
      with open(matrixFilePath, 'r') as file:
        lines = file.readlines()
        numRows = int(lines[0].strip().split('=')[1])
        numCols = int(lines[1].strip().split('=')[1])
        matrix = SparseMatrix(numRows, numCols)
        for line in lines[2:]:
          if line.strip():
            row, col, val = map(int, line.strip()[1:-1].split(','))
            matrix[(row, col)] = val
            
        return matrix
    except Exception as e:
      raise ValueError("Input file has wrong format") from e
    
  def getElement(self, row, col):
    return self.matrix.get((row, col), 0)
  
  def setElement(self, row, col, value):
    if value != 0:
      self.matrix[(row, col)] = value
    elif (row, col) in matrix:
      del self.matrix[(row, col)]
      
  def __getitem__(self, tuple):
    return self.getElement(tuple[0], tuple[1])
  
  def __setitem__(self, tuple, value):
    self.setElement(tuple[0], tuple[1], value)
    
  def __str__(self):
    result = f"rows={self.numRows}\ncols={self.numCols}\n"
    for (row, col), value in sorted(self.matrix.items()):
      result += f"({row}, {col}, {value})\n"
    return result


def main():
  matrix = SparseMatrix.load("Input/test")
  print(matrix)
  
if __name__ == "__main__":
  main()
