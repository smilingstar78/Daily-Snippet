m, n = list(map(int, input().split()))

happiness = 0

elements = [int(x) for x in input().split()]

likes = set(int(x) for x in input().split())
dislikes = set(int(y) for y in input().split())

for item in elements:
    if item in likes:
        happiness += 1
    elif item in dislikes:
        happiness -= 1

print(happiness)

#20th March, 2025, Thursday, 20th Ramadan, 10:21pm
