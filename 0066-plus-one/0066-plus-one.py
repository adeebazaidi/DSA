class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=0
        for i in digits:
            s=s*10+i
        s+=1
        l=[]
        if s == 0:
            return [0]
        while s:
            a=s%10
            l.append(a)
            s=s//10
        l.reverse()
        return l