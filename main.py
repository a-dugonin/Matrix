from matrix import Matrix

m1 = Matrix(count_rows=2, count_columns=3)
m1.matrix = [[1, 2, 3], [4, 5, 6]]
m2 = Matrix(count_rows=2, count_columns=3)
m2.matrix = [[7, 8, 9], [10, 11, 12]]
print(m1, '\n')
print(m2, '\n')
print(m1.add(m2), '\n')
print(m1.subtract(m2), '\n')
m3 = Matrix(count_rows=3, count_columns=2)
m3.matrix = [[1, 2], [3, 4], [5, 6]]
print(m3, '\n')
print(m1.multiply(m3), '\n')
print(m1.transpose())
