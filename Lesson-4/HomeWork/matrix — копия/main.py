import numpy as np

class Structure:

    def __init__(self, struct:list):
        if struct is None:
            self.struct = []
        else:
            self.struct = struct

    def __mul__(self,other):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __repr__(self):
        pass

class Matrix(Structure):

    def __init__(self, struct: list):

        try:
            if not (isinstance(struct, list) and all(isinstance(row, list) for row in struct)):
                raise ValueError("!= list[list[]]")

            row_len = len(struct[0])

            if not all(len(row) == row_len for row in struct):
                raise ValueError("len(list[1]) != len(list[2])")

            super().__init__(struct)
        except ValueError as err:
            print(err)


    def __mul__(self,other):
        try:
            if len(self.struct[0]) != len(other.struct) or not isinstance(other, Matrix):
                raise ValueError("Количество столбцов первой матрицы != количество строк второй")
            else:
                return Matrix([[sum(self.struct[i][k] * other.struct[k][j] for k in range(len(self.struct[0]))) for j in
                                range(len(other.struct[0]))] for i in range(len(self.struct))])
        except ValueError as e:
            print(e)

    def __sub__(self,other):
        try:
            if len(self.struct) != len(other.struct) or len(self.struct[0]) != len(other.struct[0]):
                raise ValueError("Матрицы не одной размерности")
            else:
                return Matrix([[self.struct[i][k] - other.struct[i][k] for k in range(len(other.struct[0]))] for i in range(len(self.struct))])
        except ValueError as e:
            print(e)

    def __add__(self, other):
        try:
            if len(self.struct) != len(other.struct) or len(self.struct[0]) != len(other.struct[0]):
                raise ValueError("Матрицы не одной размерности")
            else:
                return Matrix([[self.struct[i][k] + other.struct[i][k] for k in range(len(other.struct[0]))] for i in range(len(self.struct))])
        except ValueError as e:
            print(e)

    def __repr__(self):
        return "\n".join(str(row) for row in self.struct)

#=======================
#Задание №1
#=======================

A = Matrix([[1, 2, 4],
             [7, 5, -2],
             [-2, 1, 3]])
B = Matrix([[-1, 0, 3],
            [2, -6, 1],
            [-7, 1, 5]])
C = Matrix([[-2, 3],
            [4, 0],
            [7, -1]])

print(A+B)

print(B-A)

print(A*C)

print(A*B*C)

#=======================
#Задание №2
#=======================

A1 = Matrix([[0, 3, 4],
            [-7, 1, -2],
            [2, -1, 3]])

B1 = Matrix([[1, 2, 4],
            [7, 0, -2],
            [-3, -2, 5]])
C1 = Matrix([[-3, 2],
            [0, 4],
            [-1, 7]])

print(A1+B1)

print(B1-A1)

print(A1*C1)

print(A1*B1*C1)