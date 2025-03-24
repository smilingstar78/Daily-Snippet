from collections import namedtuple
n, cols = int(input()), input().split()
Student = namedtuple('Student', cols)
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")

#24th March,2025, Monday, 24th Ramadan, 9:58pm
