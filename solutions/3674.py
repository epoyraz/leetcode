class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        # 1) prefix sums of nums for O(1) rangeâsum
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + nums[i]

        # 2) next greater element to the right (or n if none)
        nge = [n]*n
        stack = []
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                nge[stack.pop()] = i
            stack.append(i)

        # 3) build binaryâlifting tables up[k][i] and sumLen[k][i]
        LOG = (n+1).bit_length()
        up     = [ [n]*n for _ in range(LOG) ]
        sumLen = [ [0]*n for _ in range(LOG) ]

        # k = 0
        for i in range(n):
            up[0][i] = nge[i]
            sumLen[0][i] = nums[i] * (nge[i] - i)

        # k â¥ 1
        for kk in range(1, LOG):
            u0 = up[kk-1]
            s0 = sumLen[kk-1]
            u1 = up[kk]
            s1 = sumLen[kk]
            for i in range(n):
                j = u0[i]
                if j < n:
                    u1[i] = u0[j]
                    s1[i] = s0[i] + s0[j]
                else:
                    u1[i] = n
                    s1[i] = s0[i]

        # cost(L,R) = sum_{p=L..R} max(nums[L..p]) - sum(nums[L..R])
        def cost(L, R):
            sum_a = P[R+1] - P[L]
            acc = 0
            cur = L
            for kk in reversed(range(LOG)):
                nxt = up[kk][cur]
                if nxt <= R:
                    acc += sumLen[kk][cur]
                    cur = nxt
            # last segment from cur..R all have prefixâmax = nums[cur]
            acc += nums[cur] * (R - cur + 1)
            return acc - sum_a

        # 4) for each R, binaryâsearch smallest L so cost(L,R) â¤ k
        ans = 0
        for R in range(n):
            lo, hi, best = 0, R, R+1
            while lo <= hi:
                mid = (lo + hi) // 2
                if cost(mid, R) <= k:
                    best = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            if best <= R:
                ans += (R - best + 1)
        return ans
