class Solution:
    def minimumTimeRequired(self, jobs, k):
        jobs.sort(reverse=True)
        n = len(jobs)
        res = [sum(jobs)]  # wrap in a list to make it mutable in nested scope

        def backtrack(i, workloads):
            if i == n:
                res[0] = min(res[0], max(workloads))
                return
            seen = set()
            for j in range(k):
                if workloads[j] in seen:
                    continue
                if workloads[j] + jobs[i] >= res[0]:
                    continue
                seen.add(workloads[j])
                workloads[j] += jobs[i]
                backtrack(i + 1, workloads)
                workloads[j] -= jobs[i]

        backtrack(0, [0] * k)
        return res[0]
