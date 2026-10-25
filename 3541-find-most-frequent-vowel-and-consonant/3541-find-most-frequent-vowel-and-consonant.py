class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = "aeiou"
        max_v = 0
        max_c = 0

        for ch in set(s):
            if ch in vowels:
                max_v = max(max_v, s.count(ch))
            else:
                max_c = max(max_c, s.count(ch))

        return max_v + max_c