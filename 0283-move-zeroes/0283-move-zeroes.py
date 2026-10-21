class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        while len(result) < len(nums):
            result.append(0)

        nums[:] = result
        