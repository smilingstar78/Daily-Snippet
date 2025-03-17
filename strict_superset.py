A = set(map(int, input().split()))
n = int(input())

is_strict_superset = True

for _ in range(n):
    other = set(map(int, input().split()))
    if not (A > other):  # strict superset operator!
        is_strict_superset = False
        break

print(is_strict_superset)

#17th March, 2025, Monday, 17th Ramadan, 10:21pm
