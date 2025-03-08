import numpy 

values = list(map(int, input().split()))

if len(values) == 2:
    m, n = values
    print(numpy.zeros((m, n), dtype=int))
    print(numpy.ones((m, n), dtype=int))
elif len(values) == 3:
    m, n, o = values
    print(numpy.zeros((m, n, o), dtype=int))
    print(numpy.ones((m, n, o), dtype=int))
elif len(values) == 4:
    m, n, o, p = values
    print(numpy.zeros((m, n, o, p), dtype = numpy.int))
    print(numpy.ones((m, n, o, p), dtype = numpy.int))
else:
    print("Invalid input. Enter either 2 or 3 integers.")

#8th March, 2025, Saturday, 8th Ramadan, 9:29pm
