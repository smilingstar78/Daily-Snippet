from itertools import permutations

string, num = input().split()

num = int(num)

string = sorted(string)
list1 = list(permutations(string, num))

for pair in list1:
    print(''.join(pair))

#22nd March, 2025, Saturday, 22nd Ramadan, 10:00pm
