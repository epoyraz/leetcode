from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        def can_do(k):
            # Try to assign the k easiest tasks using the k strongest workers
            ws = workers[-k:]      # take k strongest
            pills_left = pills
            # We'll keep ws as a sorted list and remove one worker per task
            for t in reversed(tasks[:k]):
                # 1) try to find a worker who can do it without a pill
                i = bisect_left(ws, t)
                if i < len(ws):
                    ws.pop(i)
                else:
                    # 2) otherwise try to find a worker who with a pill can do it
                    #    i.e. w + strength >= t  â  w >= t â strength
                    j = bisect_left(ws, t - strength)
                    if j < len(ws) and pills_left > 0:
                        ws.pop(j)
                        pills_left -= 1
                    else:
                        return False
            return True

        # binary search the maximum k
        lo, hi, ans = 0, min(n, m), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_do(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
