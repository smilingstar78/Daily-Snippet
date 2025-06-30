class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
        

# 30th June, 2025, Monday, 10:29 pm
