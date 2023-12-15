from matrix import Matrix

m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [10, 11, 12]])
m3 = Matrix([[1, 2], [3, 4], [5, 6]])
print('Матрица №1', m1, sep='\n')
print('Матрица №2', m2, sep='\n')
print('Матрица №3', m3, sep='\n')
print('Сложение матриц №1 и №2', m1.add(m2), sep='\n')
print('Вычитание из матрицы №1, матрицы №2', m1.subtract(m2), sep='\n')
print('Умножение матриц №1 и №3', m1.multiply(m3), sep='\n')
print('Транспонирование матрицы №1', m1.transpose(), sep='\n')
