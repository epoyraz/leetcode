from collections import Counter

class Solution:
    def numSquarefulPerms(self, nums):
        def is_square(n):
            r = int(n ** 0.5)
            return r * r == n

        def backtrack(x, count, depth):
            if depth == len(nums):
                return 1
            total = 0
            for y in graph[x]:
                if count[y] > 0:
                    count[y] -= 1
                    total += backtrack(y, count, depth + 1)
                    count[y] += 1
            return total

        count = Counter(nums)
        graph = {x: [] for x in count}

        for x in count:
            for y in count:
                if is_square(x + y):
                    graph[x].append(y)

        res = 0
        for x in count:
            count[x] -= 1
            res += backtrack(x, count, 1)
            count[x] += 1

        return res
