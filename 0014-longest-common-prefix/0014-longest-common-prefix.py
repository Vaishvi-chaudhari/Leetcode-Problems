class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        if strs == "":
            return ""
        for word in strs[1: ]:
            while not word.startswith(prefix):
                # Update Prefix to remove its last char (-1 means last chr, but excluded - so sec last.)
                prefix = prefix[ : -1]
        return prefix