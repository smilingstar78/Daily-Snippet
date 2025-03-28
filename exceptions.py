n = int(input())

for _ in range(n):   
    try:
        a, b = list(map(int, input().split()))
        print(a//b)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print(f"Error Code: {e}")

#28th March, 2025, Friday(Jumma tul Wida), 28th Ramadan, 8:51pm
