class Solution:
    def countServers(self, n, logs, x, queries):
        from collections import defaultdict

        # Sort logs by time
        logs.sort(key=lambda t: t[1])
        # Pair queries with their indices to return answers in order
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        ans = [0] * len(queries)

        left = 0
        right = 0
        count = defaultdict(int)
        active_servers = 0

        for q_time, q_index in sorted_queries:
            # Expand window to include logs within [q_time - x, q_time]
            while right < len(logs) and logs[right][1] <= q_time:
                server_id = logs[right][0]
                count[server_id] += 1
                if count[server_id] == 1:
                    active_servers += 1
                right += 1

            # Shrink window from left: logs with time < q_time - x
            while left < len(logs) and logs[left][1] < q_time - x:
                server_id = logs[left][0]
                count[server_id] -= 1
                if count[server_id] == 0:
                    active_servers -= 1
                left += 1

            ans[q_index] = n - active_servers

        return ans
