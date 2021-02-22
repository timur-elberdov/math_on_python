# Реализация матриц через ООП


class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

        self.__column_start = -1
        self.__row_start = -1
        self.__i = -1
        self.__l = 0

        self._rows = len(matrix)
        self._columns = len(matrix[0])

        self._is_square = True if len(matrix) == len(matrix[0]) else False

        self._is_zero = True
        for row in matrix:
            for i in row:
                if i != 0:
                    self._is_zero = False

        self._is_identity = False
        if self._is_square is True:
            for index, row in enumerate(matrix):
                if row[index] == 1 and row.count(0) == (len(row) - 1):
                    self._is_identity = True
                else:
                    self._is_identity = False

    def info(self):
        print(f'Размер: {self._rows}x{self._columns}', end=". ")
        if self._is_identity is True:
            print('Единичная')
        elif self._is_zero is True:
            print('Нулевая')
        else:
            print('')

    def __str__(self):
        str_matrix = []
        for line in self.matrix:
            str_matrix.append(f'{" ".join(map(str, line))}\n')
        return ''.join(str_matrix)

    def transpose(self):
        result_matrix = []
        for i in range(self._columns):
            line = []
            for j in range(self._rows):
                line.append(self.matrix[j][i])
            result_matrix.append(line)
        return Matrix(result_matrix)

    def __add__(self, other):
        if self._rows != other._rows or self._columns != other._columns:
            print('Невозможно выполнить сложение матриц разной размерности!')
        else:
            result_matrix = []
            for i, line in enumerate(self.matrix):
                result_matrix.append(list(map(lambda x,y: x + y, self.matrix[i], other.matrix[i])))
            return Matrix(result_matrix)

    def __sub__(self, other):
        if self._rows != other._rows or self._columns != other._columns:
            print('Невозможно выполнить вычитание матриц разной размерности!')
        else:
            result_matrix = []
            for i, line in enumerate(self.matrix):
                result_matrix.append(list(map(lambda x,y: x - y, self.matrix[i], other.matrix[i])))
            return Matrix(result_matrix)

    def __mul__(self, other):
        result_matrix = []
        if isinstance(other, Matrix) is True:
            if self._columns != other._rows:
                print('Матрицы несовместимы: число столбцов первой матрицы не равно числу строк второй!')
            else:
                for i in range(self._rows):
                    result_line = []
                    for j in range(other._columns):
                        result_num = []
                        for k in range(self._columns):
                            result_num.append(self.matrix[i][k] * other.matrix[k][j])
                        result_line.append(sum(result_num))
                    result_matrix.append(result_line)
                return Matrix(result_matrix)
        elif isinstance(other, (int, float, complex)):
            for row in self.matrix:
                result_matrix.append(list(map(lambda x: x * (other), row)))
            return Matrix(result_matrix)

    def minor(self, elem:tuple):
        result_matrix = self.matrix
        result_matrix.pop(elem[0])
        for row in result_matrix:
            row.pop(elem[1])
        return Matrix(result_matrix)

    def determinant(self):
        if self._is_square is False:
            print('Невозможно вычислить определитель неквадратной матрицы!')
        else:
            if self._rows == 2:
                det = self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
                return det
            else:
                minors = []
                for i in range(self._columns):
                    minors.append(self.minor((0, i)))
                dets = []
                for dett in minors:
                    dets.append(dett.determinant())
                res = []
                for index, i in enumerate(self.matrix[0]):
                    res.append((-1)**index*i)
                det = sum(map(lambda x, y: x*y, res, dets))
                return det


a = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
b = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
g = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
d = Matrix([[1, 0, 0]])
e = Matrix([[0, 0, 0]])
f = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]])
c = Matrix([[9, 8, 7,55, 98, 5], [6, 5, 4, 16, 14, 1], [3, 2, 1, 57, 99, 16]])

s = Matrix([[0, 1, 0, 1, 2], [3, 4, 0, 1, 2]])
l = Matrix([[0, 1, 2], [3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]])
x = s*l

print(a.determinant())
l = Matrix([[3, 4], [6, 7]])
print(a.minor((0,2)).matrix[0])

p = Matrix([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]])

print(p)
print(p.minor((2,4)))
print(l.determinant())

