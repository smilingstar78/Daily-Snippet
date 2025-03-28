import numpy

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = numpy.array(A)
B = numpy.array(B)

print(numpy.inner(A, B))
print(numpy.outer(A, B))

#28th March, 2025, Friday(Jumma tul Wida), 28th Ramadan, 8:33pm
