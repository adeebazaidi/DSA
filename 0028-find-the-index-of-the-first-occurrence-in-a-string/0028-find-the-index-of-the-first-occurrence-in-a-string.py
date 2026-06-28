class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range (len(haystack)):
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1