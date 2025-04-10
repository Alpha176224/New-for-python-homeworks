import numpy as np

# 1. Create a vector with values ranging from 10 to 49
vector_10_49 = np.arange(10, 50)
print("1. Vector (10 to 49):\n", vector_10_49)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
matrix_0_8 = np.arange(9).reshape(3, 3)
print("\n2. 3x3 Matrix (0 to 8):\n", matrix_0_8)

# 3. Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("\n3. 3x3 Identity Matrix:\n", identity_matrix)

# 4. Create a 3x3x3 array with random values
random_array_3x3x3 = np.random.random((3, 3, 3))
print("\n4. 3x3x3 Random Array:\n", random_array_3x3x3)

# 5. Create a 10x10 array with random values and find the min and max
array_10x10 = np.random.random((10, 10))
min_val = array_10x10.min()
max_val = array_10x10.max()
print("\n5. 10x10 Array Min:", min_val, "Max:", max_val)

# 6. Create a random vector of size 30 and find the mean value
vector_30 = np.random.random(30)
mean_val = vector_30.mean()
print("\n6. Mean of random vector (size 30):", mean_val)

# 7. Normalize a 5x5 random matrix
matrix_5x5 = np.random.random((5, 5))
normalized_5x5 = (matrix_5x5 - np.min(matrix_5x5)) / (np.max(matrix_5x5) - np.min(matrix_5x5))
print("\n7. Normalized 5x5 Matrix:\n", normalized_5x5)

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
product_5x2 = np.dot(matrix_5x3, matrix_3x2)
print("\n8. 5x3 * 3x2 Matrix Product:\n", product_5x2)

# 9. Create two 3x3 matrices and compute their dot product
mat1_3x3 = np.random.random((3, 3))
mat2_3x3 = np.random.random((3, 3))
dot_product_3x3 = np.dot(mat1_3x3, mat2_3x3)
print("\n9. Dot Product of Two 3x3 Matrices:\n", dot_product_3x3)

# 10. Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.random((4, 4))
transpose_4x4 = matrix_4x4.T
print("\n10. Transpose of 4x4 Matrix:\n", transpose_4x4)

# 11. Create a 3x3 matrix and calculate its determinant
matrix_det = np.random.random((3, 3))
det_value = np.linalg.det(matrix_det)
print("\n11. Determinant of 3x3 Matrix:", det_value)

# 12. Create matrices A (3x4) and B (4x3), compute A · B
A_3x4 = np.random.random((3, 4))
B_4x3 = np.random.random((4, 3))
product_A_B = np.dot(A_3x4, B_4x3)
print("\n12. Product of A (3x4) and B (4x3):\n", product_A_B)

# 13. 3x3 random matrix and 3-element column vector, compute matrix-vector product
matrix_3x3 = np.random.random((3, 3))
column_vector = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3, column_vector)
print("\n13. Matrix-Vector Product:\n", matrix_vector_product)

# 14. Solve the linear system Ax = b (A: 3x3 matrix, b: 3x1 column vector)
A_system = np.random.rand(3, 3)
b_vector = np.random.rand(3, 1)
x_solution = np.linalg.solve(A_system, b_vector)
print("\n14. Solution x to Ax = b:\n", x_solution)

# 15. Row-wise and column-wise sums of a 5x5 matrix
matrix_5x5_sums = np.random.random((5, 5))
row_sums = matrix_5x5_sums.sum(axis=1)
col_sums = matrix_5x5_sums.sum(axis=0)
print("\n15. Row-wise Sums:\n", row_sums)
print("    Column-wise Sums:\n", col_sums)
