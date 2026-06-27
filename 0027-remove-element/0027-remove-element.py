class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a=[]
        k=0
        for i in range(len(nums)):
            if nums[i]!= val:
                a.append(nums[i])
                k=k+1
        b=len(nums)-k
        while b:
            a.append('_')
            b-=1
        nums[:]=a
        return k