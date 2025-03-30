import re

def is_valid_float(s):
    # Regular expression to match valid floating-point format
    pattern = r'^[+-]?(\d*\.\d+)$'
    
    if re.match(pattern, s):
        try:
            float(s)  # Convert to float to check for exceptions
            return True
        except:
            return False
    return False

# Read input
n = int(input())
for _ in range(n):
    print(is_valid_float(input()))

#30th March, 2025, Sunday, 29th Ramadan(Chand Raat), 12:35pm
