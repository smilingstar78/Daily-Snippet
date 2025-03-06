def average(array):
    # your code goes here
    s = set()
    s.update(array)
    average = sum(s)/len(s)
    return average
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#6th March, 2025, Thursday, 6th Ramadan, 10:11pm
