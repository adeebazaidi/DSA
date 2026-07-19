class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        if num < 0:
            num &= 0xffffffff

        hex_chars = "0123456789abcdef"
        p = ""

        while num != 0:
            a = num % 16
            p = hex_chars[a] + p
            num //= 16

        return p