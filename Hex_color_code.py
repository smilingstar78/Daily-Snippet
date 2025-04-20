import re

n = int(input())
inside_block = False

for _ in range(n):
    line = input()

    # If a line ends or has only '{', we start scanning from the next line
    if '{' in line:
        inside_block = True
        continue  # skip this line

    if inside_block:
        # Use regex to find all valid hex color codes
        matches = re.findall(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b', line)
        for match in matches:
            print(match)

    # If line has '}', we exit the block
    if '}' in line:
        inside_block = False

#20th April, 2025, Sunday, 12:25pm
