import numpy as np

N = int(input())

A = np.array([list(map(int, input().split())) for _ in range(N)])

B = np.array([list(map(int, input().split())) for _ in range(N)])

print(np.matmul(A, B))

#27th March, 2025, Thursday, 27th Ramadan, 10:28pm
