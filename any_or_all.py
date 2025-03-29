n, integers = int(input()), list(map(int, input().split()))
print(all(x > 0 for x in integers) and any(str(x) == str(x)[::-1] for x in integers))

#29th March, 2025, Saturday, 29th Ramadan, 9:06pm
