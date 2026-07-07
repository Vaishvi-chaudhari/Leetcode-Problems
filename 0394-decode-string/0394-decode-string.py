class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        countStack = []
        stringStack = []
        currNum = 0
        currStr = ""

        for ch in s:
            if ch.isdigit():
                currNum = currNum * 10 + int(ch)
            elif ch == '[':
                countStack.append(currNum)
                stringStack.append(currStr)
                currNum = 0
                currStr = ""
                
            elif ch == ']':
                repeat = countStack.pop()
                prev = stringStack.pop()
                currStr = prev + currStr * repeat
            else:
                currStr += ch
        return currStr