import re

string = input()
to_find = input()

pattern = f'(?={to_find})'  

matches = re.finditer(pattern, string)

found = False
for match in matches:
    found = True
    print((match.start(), match.start() + len(to_find) - 1))

if not found:
    print((-1, -1))

#23rd March, 2025(Pakistan Day), Sunday, 23rd Ramadan, 10:40pm
