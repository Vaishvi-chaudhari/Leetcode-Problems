class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(l, r):
            if l >= r:
                return

            mid = (l + r) // 2
            merge_sort(l, mid)
            merge_sort(mid + 1, r)
            temp = []
            i, j = l, mid + 1

            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= r:
                temp.append(nums[j])
                j += 1
            nums[l:r + 1] = temp

        merge_sort(0, len(nums) - 1)
        return nums

        # n = len(nums)
        # for i in range(n):
        #     mn = nums[i]
        #     ind = i
        #     for j in range(i + 1, n):
        #         if nums[j] < mn:
        #             mn = nums[j]
        #             ind = j
        #     temp = nums[i]
        #     nums[i] = nums[ind]
        #     nums[ind] = temp
            
        # return nums

        # n = len(nums)
        # for i in range(n):
        #     isSwap = False

        #     for j in range(n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #             isSwap = True
            
        #     if not isSwap:
        #         break

        # return nums