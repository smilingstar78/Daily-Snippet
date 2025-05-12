from itertools import product

# Input
k, M = map(int, input().split())
lists = []

for _ in range(k):
    lst = list(map(int, input().split()))
    lists.append(lst[1:])  # exclude the count

# Generate all combinations and calculate the function
max_val = 0
for combo in product(*lists):
    val = sum(x**2 for x in combo) % M
    max_val = max(max_val, val)

print(max_val)

# 12th May, 2025, Monday, 8:01pm
