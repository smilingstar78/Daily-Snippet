n = int(input())
num = list(map(int, input().split()))
s1 = set(num)
op = int(input())
for i in range(op):
    operations = input().split()
    n1 = int(operations[1])
    s2 = list(map(int, input().split()))
    
    if operations[0] == 'intersection_update':
        s1.intersection_update(s2)
    elif operations[0] == 'update':
        s1.update(s2)
    elif operations[0] == 'symmetric_difference_update':
        s1.symmetric_difference_update(s2)
    elif operations[0] == 'difference_update':
        s1.difference_update(s2)
    else:
        print('Enter Valid Operation')
        
print(sum(s1)

#16th March, 2025, Sunday, 16th Ramadan, 10:00pm
