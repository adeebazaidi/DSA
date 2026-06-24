class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=[]
        for i in range(len(s)):
            if s[i].isalnum():
                s1.append(s[i].lower())

        s=s1[:]
        s1.reverse()
        if s == s1:
            return True
        else:
            return False         