from itertools import combinations

string, num = input().split()

num = int(num)

string = sorted(string)

for i in range(num):
    list1 = list(combinations(string, i+1))
    for pair in list1:
        print(''.join(pair))

#22nd March, 2025, Saturday, 22nd Ramadan, 10:14pm
