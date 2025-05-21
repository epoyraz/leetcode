class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        res = 0
        best = i = 0
        
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                best = max(best, jobs[i][1])
                i += 1
            res += best
        return res
