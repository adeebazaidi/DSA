class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0

        for i in range(1000, n + 1):
            ans += len(str(i)) // 4

        return ans