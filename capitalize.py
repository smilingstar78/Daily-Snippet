def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


#14th Marxh, 2025, Friday, 14th Ramadan, 7:20pm
