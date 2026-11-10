class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(i, xor):
            if i == len(nums):
                return xor

            include = dfs(i + 1, xor ^ nums[i])
            exclude = dfs(i + 1, xor)

            return include + exclude

        return dfs(0, 0)