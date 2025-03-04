N, M = map(int, input().split())

# Top Half
for i in range(1, N, 2):
    print((".|." * i).center(M, "-"))

# Middle Row
print("WELCOME".center(M, "-"))

# Bottom Half (Mirror of Top Half)
for i in range(N-2, 0, -2):
    print((".|." * i).center(M, "-"))
#4th March, 2025
