import numpy as np

rows, cols = map(int, input().split())  
matrix = np.array([list(map(int, input().split())) for _ in range(rows)], dtype=float) 

print(np.mean(matrix, axis=1))  
print(np.var(matrix, axis=0))  
print(f"{np.std(matrix, axis=None):.11f}")

#13th March, 2025, Thursday, 13th Ramadan, 11:43pm  
