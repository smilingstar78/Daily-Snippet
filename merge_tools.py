def merge_the_tools(string, k):
    # Loop through the string in chunks of size k
    for i in range(0, len(string), k):
        substring = string[i:i+k]  # Get the substring of length k
        unique_chars = ""  # Store unique characters in order
        
        # Iterate through the substring to remove duplicates
        for char in substring:
            if char not in unique_chars:
                unique_chars += char  # Add only unique characters
        
        print(unique_chars)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#6th March, 2025, Thursday, 6th Ramadan, 9:59pm
