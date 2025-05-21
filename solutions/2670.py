class Solution:
    def makeSubKSumEqual(self, arr, k):
        n = len(arr)
        visited = [False] * n
        total_ops = 0

        for start in range(n):
            if visited[start]:
                continue
            # Traverse the cycle starting from this index
            cycle = []
            i = start
            while not visited[i]:
                visited[i] = True
                cycle.append(arr[i])
                i = (i + k) % n

            cycle.sort()
            median = cycle[len(cycle) // 2]
            total_ops += sum(abs(x - median) for x in cycle)

        return total_ops
