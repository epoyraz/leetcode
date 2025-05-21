class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        n = len(processorTime)
        processorTime.sort()
        tasks.sort(reverse=True)
        res = 0
        for i in range(n):
            finish_time = max(processorTime[i] + tasks[4*i + j] for j in range(4))
            res = max(res, finish_time)
        return res
