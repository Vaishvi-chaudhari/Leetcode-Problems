class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        count = 0
        temp = num 
        while num > 0:
            dig = num % 10
            if dig != 0 and temp % dig == 0:
                count += 1
            num = num // 10 # num /= 10
        return count


        