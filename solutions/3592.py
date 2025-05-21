import heapq
from collections import defaultdict

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        cnt = defaultdict(int)
        top = []       # min-heap of (freq, num)
        rest = []      # max-heap of (-freq, -num)
        in_top = set()
        sum_top = [0]  # weâll do sum_top[0] += â¦ / -= â¦ inside closures

        def clean_top():
            while top:
                f, num = top[0]
                if cnt.get(num, 0) != f or num not in in_top:
                    heapq.heappop(top)
                else:
                    break

        def clean_rest():
            while rest:
                nf, nnum = rest[0]
                f, num = -nf, -nnum
                if cnt.get(num, 0) != f or num in in_top:
                    heapq.heappop(rest)
                else:
                    break

        def promote():
            clean_rest()
            if not rest: return
            nf, nnum = heapq.heappop(rest)
            f, num = -nf, -nnum
            in_top.add(num)
            heapq.heappush(top, (f, num))
            sum_top[0] += f * num

        def demote():
            clean_top()
            f, num = heapq.heappop(top)
            in_top.remove(num)
            sum_top[0] -= f * num
            heapq.heappush(rest, (-f, -num))

        def rebalance():
            distinct = len(cnt)
            target = min(x, distinct)
            # shrink top if too large
            while len(in_top) > target:
                demote()
            # grow top if too small
            while len(in_top) < target:
                promote()
            # ensure every item in top â¥ every item in rest
            while top and rest:
                clean_top(); clean_rest()
                if not top or not rest:
                    break
                f_t, num_t = top[0]
                f_r, num_r = -rest[0][0], -rest[0][1]
                if (f_t < f_r) or (f_t == f_r and num_t < num_r):
                    # swap them
                    heapq.heappop(top)
                    in_top.remove(num_t)
                    sum_top[0] -= f_t * num_t
                    heapq.heappop(rest)
                    in_top.add(num_r)
                    sum_top[0] += f_r * num_r
                    heapq.heappush(top, (f_r, num_r))
                    heapq.heappush(rest, (-f_t, -num_t))
                else:
                    break

        # Initialize counts for the first window
        for i in range(k):
            cnt[nums[i]] += 1
        # Put everything into rest, then rebalance to fill top
        for num, f in cnt.items():
            heapq.heappush(rest, (-f, -num))
        rebalance()

        ans = [sum_top[0]]

        # Slide window
        for i in range(k, n):
            old = nums[i - k]
            # remove old
            cnt[old] -= 1
            if old in in_top:
                sum_top[0] -= old
            if cnt[old] == 0:
                del cnt[old]
                in_top.discard(old)
            else:
                if old in in_top:
                    heapq.heappush(top, (cnt[old], old))
                else:
                    heapq.heappush(rest, (-cnt[old], -old))

            # add new
            new = nums[i]
            cnt[new] += 1
            if new in in_top:
                sum_top[0] += new
                heapq.heappush(top, (cnt[new], new))
            else:
                heapq.heappush(rest, (-cnt[new], -new))

            rebalance()
            ans.append(sum_top[0])

        return ans
