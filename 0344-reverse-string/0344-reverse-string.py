class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        rev=[]
        for i in range(len(s)-1,-1,-1):
            rev.append(s[i])
        for i in range (len(s)):
            s[i]=rev[i]
        return s