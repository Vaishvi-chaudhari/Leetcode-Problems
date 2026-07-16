class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        processorTime.sort()
        tasks.sort(reverse=True)

        ans = 0
        for i in range(len(processorTime)):
            ans = max(ans, processorTime[i] + tasks[i * 4])
        return ans