class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = [0] * 26
        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1
        return True

        # magazine = list(magazine)
        # for ch in ransomNote:
        #     if ch in magazine:
        #         magazine.remove(ch)
        #     else:
        #         return False
        # return True

        # freq = {}
        # for ch in magazine:
        #     freq[ch] = freq.get(ch, 0) + 1
        # for ch in ransomNote:
        #     if freq.get(ch, 0) == 0:
        #         return False
        #     freq[ch] -= 1
        # return True