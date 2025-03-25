import numpy as np

# Read input
n = int(input())  # Size of the square matrix

# Read the matrix elements
matrix = [list(map(float, input().split())) for _ in range(n)]

# Convert to NumPy array
arr = np.array(matrix)

# Compute determinant and round to 2 decimal places
determinant = round(np.linalg.det(arr), 2)

# Print result
print(determinant)

#25th March,2025, Tuesday, 25th Ramadan, 10:42pm
