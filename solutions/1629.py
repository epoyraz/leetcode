from collections import deque

class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        pos = [[] for _ in range(10)]

        # Store positions of each digit
        for i in range(n):
            pos[int(num[i])].append(i)

        used = [0] * n  # Marks if digit is already used
        res = []
        BIT = [0] * (n + 2)  # Fenwick Tree to count used positions

        # Fenwick tree helpers
        def update(i):
            i += 1
            while i < len(BIT):
                BIT[i] += 1
                i += i & -i

        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += BIT[i]
                i -= i & -i
            return s

        for _ in range(n):
            for d in range(10):
                if not pos[d]:
                    continue
                idx = pos[d][0]
                moved = idx - query(idx)
                if moved <= k:
                    k -= moved
                    res.append(str(d))
                    update(idx)
                    pos[d].pop(0)
                    break

        return ''.join(res)
