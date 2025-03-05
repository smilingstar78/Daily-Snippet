from collections import OrderedDict

N = int(input())  # Number of inputs
word_counts = OrderedDict()  # Maintain order of insertion

for _ in range(N):
    word = input().strip()
    word_counts[word] = word_counts.get(word, 0) + 1  # Increment count

# Print number of unique words
print(len(word_counts))

# Print occurrences in order of appearance
print(" ".join(map(str, word_counts.values())))

#5th March,2025, Wednesday, 5th Ramadan, 9:52pm
