class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1= sorted(s)
        s2= sorted(t)

        if s1==s2:
            return True
        else:
            return False
