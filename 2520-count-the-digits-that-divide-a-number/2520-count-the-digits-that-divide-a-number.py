class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num 
        count = 0
        while num > 0:
            dig = num % 10
            if dig != 0 and temp % dig == 0:
                count += 1
            num = num // 10
        return count


        