class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            s=0
            while num>0:
                a=num%10
                s=s+a
                num=num//10
            num=s
        return num