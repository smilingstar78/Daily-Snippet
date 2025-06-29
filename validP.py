import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.s = s
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if s == s[::-1]:
            return True
        else:
            return False
        
# 29th June, 2025, Sunday, 9:52 pm
