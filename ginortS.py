# Enter your code here. Read input from STDIN. Print output to STDOUT
def my_func(char):
    if char.islower():
        return(0,char)
    elif char.isupper():
        return(1, char)
    elif char.isdigit():
        if int(char)%2!=0:
            return(2,char)
        else:
            return(3,char)
    
s = input()

sort = sorted(s, key=my_func)
print(''.join(sort))

#29th March, 2025, Saturday, 25th Ramadan, 9:23pm
