import numpy

n,m = list(map(int, input().split()))

my_arr = []

for _ in range(n):
    
    rows = list(map(int, input().split()))
    
    data = numpy.array(rows)
    my_arr.append(data)
    
print(numpy.mean(my_arr, axis=1))
print(numpy.var(my_arr, axis=0))
result = numpy.std(my_arr, axis=None)
print(round(result, 11))

#27th March, 2025, Thursday, 27th Ramadan, 9:49pm
