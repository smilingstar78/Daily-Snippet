class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.s = s
        self.t = t
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        

        
# 30th June, 2025, Monday, 10:18 pm
