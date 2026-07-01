class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in nums:
            flag=0
            for j in nums:
                if i==j:
                    flag+=1
                    if flag > 1:
                        break
            if flag==1:
                return i