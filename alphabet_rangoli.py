import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        # Create the left side + center
        left = alphabet[size-1:i:-1]
        center = alphabet[i]
        right = alphabet[i+1:size]
        row = '-'.join(left + center + right)
        # Center the row
        lines.append(row.center(4*size - 3, '-'))

    # Mirror vertically
    full_rangoli = lines[::-1][:-1] + lines

    # Print the final rangoli
    for line in full_rangoli:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#9th April, 2025, Wednesday, 10:15pm
