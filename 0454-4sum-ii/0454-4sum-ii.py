class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sum_dict = {}
        # Store Each sum pair for nums1 and nums2:
        for i in nums1:
            for j in nums2:
                pair_sum = i + j
                sum_dict[pair_sum] = sum_dict.get(pair_sum, 0) + 1 # dict.get(key, def_value) - If key - return key's val, else def_val
        count = 0

        # Find Complementary pair of i and j (k and l) :
        for k in nums3:
            for l in nums4:
                target = - (k+l)
                if target in sum_dict:
                    count = count + sum_dict[target]
        return count