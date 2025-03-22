from itertools import groupby

s = input()

for key, group in groupby(s):
    count = len(list(group))
    print(f'({count}, {key})', end=' ')

#22nd March, 2025, Saturday, 22nd Ramadan, 10:31pm
