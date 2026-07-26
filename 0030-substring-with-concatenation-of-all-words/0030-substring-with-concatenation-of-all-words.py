class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        window_len = word_len * total_words
        target = Counter(words)
        ans = []

        for offset in range(word_len):
            left = right = offset
            window = defaultdict(int)
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in target:
                    window[word] += 1
                    count += 1
                    while window[word] > target[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        ans.append(left)
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    window.clear()
                    count = 0
                    left = right

        return ans