import email.utils
import re

pattern = r'^[a-zA-Z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

n = int(input())
for _ in range(n):
    input_line = input()
    name, addr = email.utils.parseaddr(input_line)
    
    if re.match(pattern, addr):
        print(email.utils.formataddr((name, addr)))

#17th March, 2025, Monday, 17th Ramadan, 10:31pm
