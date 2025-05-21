from collections import deque

class Solution:
    def findLexSmallestString(self, s, a, b):
        n = len(s)
        seen = set([s])
        dq = deque([s])
        best = s

        while dq:
            cur = dq.popleft()
            # update best
            if cur < best:
                best = cur

            # Operation 1: add 'a' to all odd indices
            lst = list(cur)
            for i in range(1, n, 2):
                lst[i] = str((int(lst[i]) + a) % 10)
            added = ''.join(lst)
            if added not in seen:
                seen.add(added)
                dq.append(added)

            # Operation 2: rotate right by b
            rotated = cur[-b:] + cur[:-b]
            if rotated not in seen:
                seen.add(rotated)
                dq.append(rotated)

        return best
