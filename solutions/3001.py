class Solution(object):
    def maximumScore(self, nums, k):
        mod = 10**9+7
        n = len(nums)

        # sieve for smallest prime factor up to max(nums)
        maxv = max(nums)
        spf = list(range(maxv+1))
        i = 2
        while i*i <= maxv:
            if spf[i] == i:
                j = i*i
                while j <= maxv:
                    if spf[j] == j:
                        spf[j] = i
                    j += i
            i += 1

        # primeâscore for each nums[i]
        A = [0]*n
        for idx, v in enumerate(nums):
            cnt = 0
            prev = 0
            x = v
            while x > 1:
                p = spf[x]
                if p != prev:
                    cnt += 1
                    prev = p
                x //= p
            A[idx] = cnt

        # prev greater or equal
        L = [-1]*n
        st = []
        for i in range(n):
            while st and A[st[-1]] < A[i]:
                st.pop()
            L[i] = st[-1] if st else -1
            st.append(i)

        # next strictly greater
        R = [n]*n
        st = []
        for i in range(n-1, -1, -1):
            while st and A[st[-1]] <= A[i]:
                st.pop()
            R[i] = st[-1] if st else n
            st.append(i)

        # count of subarrays where i is chosen
        counts = [0]*n
        for i in range(n):
            counts[i] = (i - L[i]) * (R[i] - i)

        # pick up to k factors in descending nums order
        idxs = list(range(n))
        idxs.sort(key=lambda i: nums[i], reverse=True)

        res = 1
        rem = k
        for i in idxs:
            if rem <= 0:
                break
            t = counts[i] if counts[i] < rem else rem
            res = res * pow(nums[i], t, mod) % mod
            rem -= t

        return res
