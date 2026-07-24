class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
            
        need = Counter(t)          
        window = {}
        have = 0                   
        required = len(need)
        left = 0
        min_len = float('inf')
        res = [-1, -1]

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = [left, right]
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if min_len != float('inf') else ""