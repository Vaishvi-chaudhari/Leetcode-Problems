class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def backtrack(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return

            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                backtrack(j + 1, parts + [part])

        backtrack(0, [])
        return res