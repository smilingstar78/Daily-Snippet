def is_leap(year):
      if year % 4 == 0:  # Check if divisible by 4
        if year % 100 == 0:  # If divisible by 100
            if year % 400 == 0:  # If divisible by 400
                return True
            else:
                return False
        else:
            return True
      else:
        return False

year = int(input())
print(is_leap(year))

#10th March, 2025, Monday, 10th Ramadan, 10:20pm
