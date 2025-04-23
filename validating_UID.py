import re

def is_valid(uid):
    # Check for length
    if len(uid) != 10:
        return False
    # Check for only alphanumeric characters
    if not uid.isalnum():
        return False
    # Check for no repetition
    if len(set(uid)) != len(uid):
        return False
    # Check for at least 2 uppercase letters
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    # Check for at least 3 digits
    if len(re.findall(r'\d', uid)) < 3:
        return False
    return True

# Input handling
n = int(input())
for _ in range(n):
    uid = input().strip()
    print("Valid" if is_valid(uid) else "Invalid")


# 23rd April, 2025, Wednesday, 10:23pm
