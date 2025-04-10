import numpy as np

# 1. Vector with values from 10 to 49
vector_10_49 = np.arange(10, 50)

# 2. 3x3 matrix with values from 0 to 8
matrix_0_8 = np.arange(9).reshape(3, 3)

# 3. 3x3 identity matrix
identity_3x3 = np.eye(3)

# 4. 3x3x3 array with random values
array_3x3x3 = np.random.rand(3, 3, 3)

# 5. 10x10 array with random values, min and max
array_10x10 = np.random.rand(10, 10)
min_val = array_10x10.min()
max_val = array_10x10.max()

# 6. Random vector of size 30, mean value
random_vector_30 = np.random.rand(30)
mean_val = random_vector_30.mean()

# 7. Normalize a 5x5 random matrix
matrix_5x5 = np.random.rand(5, 5)
normalized_5x5 = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())

# 8. Multiply 5x3 matrix by 3x2 matrix
mat_5x3 = np.random.rand(5, 3)
mat_3x2 = np.random.rand(3, 2)
product_5x2 = np.dot(mat_5x3, mat_3x2)

# 9. Dot product of two 3x3 matrices
mat1_3x3 = np.random.rand(3, 3)
mat2_3x3 = np.random.rand(3, 3)
dot_product_3x3 = np.dot(mat1_3x3, mat2_3x3)

# 10. Transpose of a 4x4 matrix
matrix_4x4 = np.random.rand(4, 4)
transpose_4x4 = matrix_4x4.T

# 11. Determinant of a 3x3 matrix
matrix_det_3x3 = np.random.rand(3, 3)
det_3x3 = np.linalg.det(matrix_det_3x3)

# 12. Matrix product of A (3x4) and B (4x3)
A_3x4 = np.random.rand(3, 4)
B_4x3 = np.random.rand(4, 3)
product_AB = np.dot(A_3x4, B_4x3)

# 13. Matrix-vector product (3x3 matrix and 3-element column vector)
matrix_3x3 = np.random.rand(3, 3)
vector_3 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, vector_3)

# 14. Solve Ax = b for 3x3 matrix A and 3x1 vector b
A_sys = np.random.rand(3, 3)
b_sys = np.random.rand(3)
x_solution = np.linalg.solve(A_sys, b_sys)

# 15. Row-wise and column-wise sums of a 5x5 matrix
matrix_5x5_sum = np.random.rand(5, 5)
row_sums = matrix_5x5_sum.sum(axis=1)
col_sums = matrix_5x5_sum.sum(axis=0)
