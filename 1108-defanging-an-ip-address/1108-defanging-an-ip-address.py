class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans_str = ""
        for ch in address:
            if ch == '.':
                ans_str += '[.]'
            else:
                ans_str += ch
        return ans_str