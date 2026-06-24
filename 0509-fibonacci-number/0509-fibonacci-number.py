class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        if n==0:
            return 0
        if n>1:
            for i in range(n-2):
                s=a+b
                a=b
                b=s
        s=a+b
        return s