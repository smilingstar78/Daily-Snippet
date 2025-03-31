import re

# Read number of test cases
t = int(input())

for _ in range(t):
    pattern = input().strip()
    try:
        re.compile(pattern)  # Check if it's a valid regex
        print(True)
    except re.error:
        print(False)

#31st March, 2025, Monday(Eid-ul-Fitr Day # 01), 1st Shiwaal, 10:36pm
