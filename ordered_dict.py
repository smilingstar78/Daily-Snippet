N = int(input())

items = {}

for i in range(N):
    item_name, item_price = input().rsplit(maxsplit=1)
    item_name = item_name.upper()
    item_price = int(item_price)
    
    if item_name in items:
        items[item_name] += item_price
    else:
        items[item_name] = item_price
for name, price in items.items():
    print(name, price)

#5th march,2025 Wednesday, 5th Ramadan, 9:37pm
