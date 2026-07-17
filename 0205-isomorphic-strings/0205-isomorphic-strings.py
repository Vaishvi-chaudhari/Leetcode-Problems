class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):

            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                if c2 in t_to_s:
                    return False
                s_to_t[c1] = c2
                t_to_s[c2] = c1

        return True

        # n = len(s)
        # for i in range(n):
        #     for j in range(i):
        #         if s[i] == s[j] and t[i] != t[j]:
        #             return False

        #         if s[i] != s[j] and t[i] == t[j]:
        #             return False
        # return True