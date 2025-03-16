from collections import Counter

n = int(input())
room = list(map(int, input().split()))

count = Counter(room)

for num in room:
    if count[num] == 1:
        print(num)

#16th March, 2025, Sunday, 16th Ramadan, 10:16pm
