class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        words = set(wordList)
        if endWord not in words:
            return []

        parent = defaultdict(list)
        q = deque([beginWord])
        words.discard(beginWord)
        found = False

        while q and not found:
            next_level = set()

            for _ in range(len(q)):
                word = q.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i + 1:]
                        if new_word in words:
                            next_level.add(new_word)
                            parent[new_word].append(word)

            words -= next_level
            q.extend(next_level)

            if endWord in next_level:
                found = True
        if not found:
            return []

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return
            for prev in parent[word]:
                path.append(prev)
                dfs(prev, path)
                path.pop()

        dfs(endWord, [endWord])

        return ans