n = int(input())
roll1 = list(map(int, input().split()))

b = int(input())
roll2 = list(map(int, input().split()))

s1 = set(roll1)
s2 = set(roll2)

print(len(s1.symmetric_difference(s2)))

#16th March, 2025, Sunday, 16th Ramadan, 9:49pm
