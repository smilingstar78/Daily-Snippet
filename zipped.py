N, X = list(map(int, input().split()))

scores = [list(map(float, input().split()))for _ in range(X)]

students_scores = zip(*scores)

for students in students_scores:
    print(sum(students)/len(students))

#15th March, 2025, Saturday, 15th Ramadan, 10:09pm
