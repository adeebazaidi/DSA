class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        bucket=[0]*26
        for i in s:
            bucket[ord(i)-97]+=1
        for i in t:
            bucket[ord(i)-97]-=1
        
        return all(x==0 for x in bucket)