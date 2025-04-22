def wrapper(f):
    def fun(l):
        formatted = []
        for number in l:
            # Get the last 10 digits
            number = number[-10:]
            # Format to +91 xxxxx xxxxx
            formatted.append(f'+91 {number[:5]} {number[5:]}')
        # Call the original function with formatted list
        return f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
