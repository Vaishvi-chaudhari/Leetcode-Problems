class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        for ch in t:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] -= 1
        
        for i in freq.values():
            if i != 0:
                return False
        return True