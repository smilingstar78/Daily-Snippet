n = int(input())  # Read number of elements
my_set = set(map(int, input().split()))  # Read set elements

num_commands = int(input())  # Read number of commands

for _ in range(num_commands):
    command = input().split()  # Read the command

    if command[0] == "pop":
        if my_set:
            my_set.remove(min(my_set))  # Ensure `pop()` removes the smallest element
    elif command[0] == "remove":
        com = int(command[1])
        if com in my_set:
            my_set.remove(com)  # Remove only if exists (avoids KeyError)
    elif command[0] == "discard":
        my_set.discard(int(command[1]))  # Safe removal (no KeyError)

print(sum(my_set))

#9th March, 2025, Sunday, 9th Ramadan, 9:48pm
