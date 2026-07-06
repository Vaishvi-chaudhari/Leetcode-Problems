class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            curr_char = chars[read]
            count = 0
            
            while read < n and chars[read] == curr_char:
                read += 1
                count += 1

            chars[write] = curr_char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write