class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = (s.strip()).split()
        s.reverse()
        return " ".join(s)

        # words = []
        # n = len(s)
        # i = 0

        # # extract words 
        # while i < n:

        #     # skip spaces
        #     while i < n and s[i] == ' ':
        #         i += 1

        #     word = ""

        #     while i < n and s[i] != ' ':
        #         word += s[i]
        #         i += 1

        #     if word != "":
        #         words.append(word)

        # # Reverse
        # left = 0
        # right = len(words) - 1

        # while left < right:
        #     words[left], words[right] = words[right], words[left]
        #     left += 1
        #     right -= 1

        # # final ans
        # ans = ""
        # for i in range(len(words)):
        #     ans += words[i]

        #     if i != len(words) - 1:
        #         ans += " "

        # return ans