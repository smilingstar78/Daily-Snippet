from collections import defaultdict

# Input
n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]

# defaultdict to store positions for each word in group A
d = defaultdict(list)

# Populate the defaultdict
for idx, word in enumerate(group_a):
    d[word].append(idx + 1)  # using 1-based indexing

# Check for each word in group B
for word in group_b:
    if word in d:
        print(' '.join(map(str, d[word])))
    else:
        print(-1)

#19th March, 2025, Wednesday, 19th Ramadan, 10:42pm
