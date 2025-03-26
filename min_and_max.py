import numpy

n, m = list(map(int, input().split()))

data = []

for _ in range(n):
    rows = list(map(int, input().split()))
    
    data.append(rows)

my_array = numpy.array(data)
minimum = numpy.min(my_array, axis=1)
    
print(numpy.max(minimum))

#26th March, 2025, Wednesday, 26th Ramadan, 11:29pm
