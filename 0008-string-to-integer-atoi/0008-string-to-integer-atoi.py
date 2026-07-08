class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0

        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        ans = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            if ans > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            ans = ans * 10 + digit
            i += 1

        return sign * ans