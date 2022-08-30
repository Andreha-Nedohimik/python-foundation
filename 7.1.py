class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'''.join(map(lambda r: '  '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda m_1, m_2: map(lambda x, y: x + y, m_1, m_2), self.matrix, other.matrix))


matrix_1 = Matrix([[1, 2, 5], [3, 4, 5], [1, 2, 5]])
matrix_2 = Matrix([[1, 2, 6], [3, 4, 6], [6, 6, 6]])
print(matrix_1)
print(matrix_2)
print(matrix_2 + matrix_1)
