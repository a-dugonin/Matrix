from numpy import array, add, subtract, matmul, transpose


class Matrix:
    """ Класс для создания экземпляров матриц """
    def __init__(self, matrix: array = None):
        self.matrix = array(matrix)

    def add(self, another_matrix: array = None) -> array:
        add_matrix = add(self.matrix, another_matrix.matrix)
        return '\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in add_matrix])

    def subtract(self, another_matrix: array = None) -> array:
        subtract_matrix = subtract(self.matrix, another_matrix.matrix)
        return '\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in subtract_matrix])

    def multiply(self, another_matrix: array = None) -> array:
        multiply_matrix = matmul(self.matrix, another_matrix.matrix)
        return '\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in multiply_matrix])

    def transpose(self) -> array:
        transposed_matrix = transpose(self.matrix)
        return '\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in transposed_matrix])

    def __str__(self):
        return '\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in self.matrix])


def main():
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 8, 9], [10, 11, 12]])
    print('Матрица №1', m1, sep='\n')
    print('Матрица №2', m2, sep='\n')
    print('Сложение матриц №1 и №2', m1.add(m2), sep='\n')
    print('Вычитание из матрицы №1, матрицы №2', m1.subtract(m2), sep='\n')
    m3 = Matrix([[1, 2], [3, 4], [5, 6]])
    print('Матрица №3', m3, sep='\n')
    print('Умножение матриц №1 и №3', m1.multiply(m3), sep='\n')
    print('Транспонирование матрицы №1', m1.transpose(), sep='\n')


if __name__ == '__main__':
    main()
