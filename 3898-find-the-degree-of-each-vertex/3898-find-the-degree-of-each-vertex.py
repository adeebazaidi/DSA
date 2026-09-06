class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        for r in matrix:
            ans.append(sum(r))
        return ans