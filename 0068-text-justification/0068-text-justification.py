class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        i = 0
        n = len(words)

        while i < n:
            line = []
            length = 0

            while i < n and length + len(line) + len(words[i]) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            if i == n or len(line) == 1:
                currentLine = " ".join(line)
                currentLine += " " * (maxWidth - len(currentLine))
                result.append(currentLine)
                continue

            spaces = maxWidth - length
            gaps = len(line) - 1
            evenSpaces = spaces // gaps
            extraSpaces = spaces % gaps
            currentLine = []

            for j in range(gaps):
                currentLine.append(line[j])
                currentLine.append(" " * (evenSpaces + (1 if j < extraSpaces else 0)))
            currentLine.append(line[-1])
            result.append("".join(currentLine))

        return result