class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        ans = []

        for word in words:
            w = word.lower()

            if all(ch in row1 for ch in w):
                ans.append(word)
            elif all(ch in row2 for ch in w):
                ans.append(word)
            elif all(ch in row3 for ch in w):
                ans.append(word)

        return ans