class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        stack = []
        seen = set()

        for ch in s:
            freq[ch] -= 1
            if ch in seen:
                continue

            while (stack and ch < stack[-1] and freq[stack[-1]] > 0):
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)

        return "".join(stack)