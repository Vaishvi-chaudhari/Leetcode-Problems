class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # magazine = list(magazine)
        # for ch in ransomNote:
        #     if ch in magazine:
        #         magazine.remove(ch)
        #     else:
        #         return False
        # return True

        freq = {}
        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in ransomNote:
            if freq.get(ch, 0) == 0:
                return False
            freq[ch] -= 1
        return True