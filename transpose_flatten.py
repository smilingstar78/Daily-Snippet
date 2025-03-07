N , M = list(map(int, input().split()))
import numpy as np
matrix = [list(map(int, input().split())) for _ in range(N)]
arr = np.array(matrix)
print(arr.transpose()) 
print(arr.flatten())

#7th March, 2025, Friday, 7th Ramadan, 9:14pm
