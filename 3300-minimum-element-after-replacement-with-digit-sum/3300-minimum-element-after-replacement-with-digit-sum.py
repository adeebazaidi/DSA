class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]

        for i in range(len(nums)):
            sum = 0

            while nums[i] != 0:
                a = nums[i] % 10
                sum = sum + a
                nums[i] = nums[i] // 10

            if sum <= min:
                min = sum

        return min