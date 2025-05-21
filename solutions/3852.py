import sys
from bisect import bisect_right
def readints():
    return map(int, sys.stdin.readline().split())

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Sort nodes by value, but remember original indices.
        order = sorted(range(n), key=lambda i: nums[i])
        vals  = [nums[i] for i in order]
        # map original index -> position in sorted array
        pos   = [0]*n
        for j,i in enumerate(order):
            pos[i] = j

        # Build component ids by checking gaps > maxDiff
        comp = [0]*n
        cid = 0
        for j in range(1,n):
            if vals[j]-vals[j-1] > maxDiff:
                cid += 1
            comp[j] = cid

        # Precompute for each j the farthest index we can reach in one hop forward
        # i.e. largest k>j with vals[k] <= vals[j] + maxDiff
        nxt = [j for j in range(n)]
        for j in range(n):
            # binary search the first index > vals[j]+maxDiff
            k = bisect_right(vals, vals[j] + maxDiff) - 1
            nxt[j] = k

        # And similarly backward
        prv = [j for j in range(n)]
        for j in range(n):
            # first index where vals[idx] >= vals[j] - maxDiff
            low = bisect_right(vals, vals[j]-maxDiff-1)
            prv[j] = low

        # Build binary lifting tables
        LOG = (n-1).bit_length()
        jump_f = [nxt]
        jump_b = [prv]
        for k in range(1, LOG):
            prev_f = jump_f[k-1]
            prev_b = jump_b[k-1]
            cur_f = [0]*n
            cur_b = [0]*n
            for j in range(n):
                cur_f[j] = prev_f[prev_f[j]]
                cur_b[j] = prev_b[prev_b[j]]
            jump_f.append(cur_f)
            jump_b.append(cur_b)

        ans = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            # if same node
            if pu == pv:
                ans.append(0)
                continue
            # if not even in same component
            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue
            # ensure pu < pv for forward jumps
            if pu < pv:
                cur = pu
                steps = 0
                # greedy lift: try the largest 2^k jump that stays below pv
                for k in reversed(range(LOG)):
                    to = jump_f[k][cur]
                    if to < pv:
                        cur = to
                        steps += (1<<k)
                # one more hop gets us >= pv
                ans.append(steps+1)
            else:
                cur = pu
                steps = 0
                for k in reversed(range(LOG)):
                    to = jump_b[k][cur]
                    if to > pv:
                        cur = to
                        steps += (1<<k)
                ans.append(steps+1)

        return ans