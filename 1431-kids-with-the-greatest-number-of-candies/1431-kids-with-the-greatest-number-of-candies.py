class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        result = []
        max_candies = candies[0]
        for i in range (len(candies)):
            if candies[i] > max_candies:
                max_candies = candies[i]

        for j in range (len(candies)):
                if candies[j] + extraCandies >= max_candies:
                    result.append(True)
                else:
                    result.append(False)
        
        return result

