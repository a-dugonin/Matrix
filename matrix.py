from numpy import array, add, subtract, matmul, transpose


class Matrix:
    def __init__(self, count_rows, count_columns, matrix: array = None):
        self.count_rows = count_rows
        self.count_columns = count_columns
        self.matrix = array(matrix)

    def add(self, another_matrix):
        add_matrix = add(self.matrix, another_matrix.matrix)
        return f'{'\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in add_matrix])}'

    def subtract(self, another_matrix):
        subtract_matrix = subtract(self.matrix, another_matrix.matrix)
        return f'{'\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in subtract_matrix])}'

    def multiply(self, another_matrix):
        dot_matrix = matmul(self.matrix, another_matrix.matrix)
        return f'{'\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in dot_matrix])}'

    def transpose(self):
        transposed_matrix = transpose(self.matrix)
        return f'{'\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in transposed_matrix])}'

    def __str__(self):
        return '\n'.join([' '.join([str(value).ljust(3) for value in row]) for row in self.matrix])


def main():
    m1 = Matrix(count_rows=2, count_columns=3)
    m1.matrix = [[1, 2, 3], [4, 5, 6]]
    m2 = Matrix(count_rows=2, count_columns=3)
    m2.matrix = [[7, 8, 9], [10, 11, 12]]
    print(m1)
    print()
    print(m2)
    print()
    print(m1.add(m2))
    print()
    print(m1.subtract(m2))
    print()
    m3 = Matrix(count_rows=3, count_columns=2)
    m3.matrix = [[1, 2], [3, 4], [5, 6]]
    print(m3)
    print()
    print(m1.multiply(m3))
    print()
    print(m1.transpose())


if __name__ == '__main__':
    main()
