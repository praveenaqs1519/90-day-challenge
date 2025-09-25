import numpy as np

v1 = np.array([[1,5],[5,8]])
v2 = np.array([[5,1],[7,8]])

print(v1 + v2)
print(np.dot(v1, v2))




A = np.array([[1, 2], [3, 4]])

# Determinant
det = np.linalg.det(A)
print("Determinant:", det)  # -2.0

# Inverse
inv = np.linalg.inv(A)
print("Inverse:\n", inv)
