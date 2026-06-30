class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rowstart = 0
        rowend = len(matrix) - 1

        colstart = 0
        colend = len(matrix[0]) - 1

        ans = []

        while rowstart <= rowend and colstart <= colend:
            # Left -> Right
            # Rowstart : colstart --> colend
            for j in range(colstart, colend + 1):
                ans.append(matrix[rowstart][j])
            rowstart += 1

            # Top -> Bottom
            # colend : rowstart --> rowend
            for i in range(rowstart, rowend + 1):
                ans.append(matrix[i][colend])
            colend -= 1

            # Right -> Left
            # rowend : colend --> colstart
            if rowstart <= rowend:
                for j in range(colend, colstart - 1, -1):
                    ans.append(matrix[rowend][j])
                rowend -= 1

            # Bottom -> Top
            # colstart : rowend --> rowstart
            if colstart <= colend:
                for i in range(rowend, rowstart - 1, -1):
                    ans.append(matrix[i][colstart])
                colstart += 1

        return ans
