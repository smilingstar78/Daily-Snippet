import numpy as np

n, m, p = map(int, input().split())  # Read dimensions: n (rows of first array), m (rows of second array), p (columns)

arrays = []  # List to store arrays

for _ in range(n + m):  # Read both arrays
    row = list(map(int, input().split()))  # Read a row
    arrays.append(row)  # Store it

# Convert list of lists into a NumPy array
arrays_np = np.array(arrays)

# Concatenation along axis 0 (vertically stacking)
print(arrays_np)

#26th March, 2025, Wednesday, 26th Ramadan, 11:16pm
