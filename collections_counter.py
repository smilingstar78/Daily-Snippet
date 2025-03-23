from collections import Counter

# Input the number of shoes
n = int(input())

# Input the shoe sizes and count their frequency
shoe_sizes = Counter(map(int, input().split()))

# Input the number of customers
customers = int(input())

total_money = 0

for _ in range(customers):
    size, price = map(int, input().split())
    
    if shoe_sizes[size] > 0:
        total_money += price
        shoe_sizes[size] -= 1  # Decrease the stock for that shoe size

print(total_money)

#23rd March, 2025(Pakistan Day), Sunday, 23rd Ramadan, 10:20pm
