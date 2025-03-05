from collections import deque

N = int(input())
de = deque()

for _ in range(N):
    user = input().split()  

    command = user[0]
    
    if command == "append":
        de.append(int(user[1]))  
    elif command == "appendleft":
        de.appendleft(int(user[1]))  
    elif command == "pop":
        de.pop()  
    elif command == "popleft":
        de.popleft()  
    else:
        print("Enter Valid Operation!")  

print(" ".join(map(str, de)))

#5th March,2025, Wednesday, 5th Ramadan, 10:16pm 
