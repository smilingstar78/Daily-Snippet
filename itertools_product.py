from itertools import product

# Read input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute Cartesian product
result = list(product(A, B))

# Print output in required format
print(" ".join(map(str, result)))

#2nd April, 2025, 3rd Day of Eid ul Fitr, Wednesday, 2:53pm
