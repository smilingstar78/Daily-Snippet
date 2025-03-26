import numpy

n, m = list(map(int, input().split()))

data = []

for _ in range(n):
    row = list(map(int, input().split()))  
    data.append(row)  

array_2d = numpy.array(data)
another_array = numpy.sum(array_2d, axis=0)
print(numpy.product(another_array))

#26th March,2025, Wednesday, 26th Ramadan, 11:23pm
