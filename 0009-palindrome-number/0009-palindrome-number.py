class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
            
        n,rev=x,0
        while n!=0:
            a=n%10
            rev=rev*10+a
            n=n//10
        if x==rev:
            return True
        else:
            return False
        
        