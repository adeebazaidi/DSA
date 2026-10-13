class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s1= sorted(s)
        # s2= sorted(t)

        if len(s)!=len(t):
            return False
        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
        return True      