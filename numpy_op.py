import numpy
row_and_col = list(map(int, input().split()))
if len(row_and_col) == 2:
    m, n = row_and_col
    A = [list(map(int,input().split()))for _ in range(m)]
    arr1 = numpy.array((A)).reshape(m ,n)

    B = [list(map(int, input().split()))for _ in range(m)]
    arr2 = numpy.array((B)).reshape(m, n) 
    
    print(arr1+arr2)
    print(arr1-arr2)
    print(arr2*arr1)
    print(arr1//arr2)
    print(arr1%arr2)
    print(arr1**arr2)

#9th March, 2025, Sunday, 9th Ramadan, 9:10am
