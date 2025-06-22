import re

s = input()

pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'

matches = re.findall(pattern, s)

if matches:
    for m in matches:
        print(m)
else:
    print(-1)

# 22nd June, 2025, Sunday, 10:22pm
