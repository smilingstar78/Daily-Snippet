n = int(input())

for i in range(n):
    elements1 = int(input())
    set1 = list(map(int, input().split()))
    elements2 = int(input())
    set2 = list(map(int, input().split()))
    set1 = set(set1)
    set2 = set(set2)
    if set1.issubset(set2):
        print(True)
    else:
        print(False)

#17th March, 2025, Monday, 17th Ramadan, 10:04pm
