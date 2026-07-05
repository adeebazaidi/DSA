class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            s = 0

            while n:
                a = n % 10
                s = s + a * a
                n = n // 10

            n = s

        if n == 1:
            return True
        else:
            return False