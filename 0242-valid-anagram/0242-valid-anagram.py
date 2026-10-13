class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s1= sorted(s)
        # s2= sorted(t)

        if sorted(s)==sorted(t):
            return True
        else:
            return False
