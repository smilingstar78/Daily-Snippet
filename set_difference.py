M = int(input())
s1 = list(map(int, input().split()))
a = set()
a.update(s1)

N = int(input())
s2 = list(map(int, input().split()))
b = set()
b.update(s2)

differ = a.symmetric_difference(b)
differ1 = sorted(differ)
for i in range(len(differ1)):
    print(differ1[i])

#6th March, 2025, Thursday, 6th Ramadan, 10:26pm
