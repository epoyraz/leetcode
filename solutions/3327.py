class Solution(object):
    def minimumMoves(self, nums, k, maxChanges):
        """
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """
        n = len(nums)
        cnt = [0] * (n + 1)      # prefix count of 1s
        s = [0] * (n + 1)        # prefix sum of indices of 1s
        for idx, v in enumerate(nums, 1):     # 1-indexed
            cnt[idx] = cnt[idx - 1] + v
            s[idx] = s[idx - 1] + idx * v

        INF = 1 << 60
        ans = INF

        for i in xrange(1, n + 1):            # Alice stands at i (1-indexed)
            need = k - nums[i - 1]            # ones still needed after free pickup
            moves = 0

            # take from immediate neighbours if possible (cost 1 each)
            for j in (i - 1, i + 1):
                if need and 1 <= j <= n and nums[j - 1]:
                    need -= 1
                    moves += 1

            # create at neighbours, then swap in (cost 2 each)
            c = min(need, maxChanges)
            need -= c
            moves += c * 2

            if need <= 0:
                ans = min(ans, moves)
                continue

            # binary-search minimal radius to collect remaining ones
            left, right = 2, max(i - 1, n - i)
            while left <= right:
                mid = (left + right) >> 1

                l1, r1 = max(1, i - mid), max(0, i - 2)
                l2, r2 = min(n + 1, i + 2), min(n, i + mid)

                c1 = cnt[r1] - cnt[l1 - 1] if r1 >= l1 else 0
                c2 = cnt[r2] - cnt[l2 - 1] if r2 >= l2 else 0

                if c1 + c2 >= need:
                    # distance cost on the left
                    sum_left = s[r1] - s[l1 - 1] if r1 >= l1 else 0
                    dist_left = c1 * i - sum_left
                    # distance cost on the right
                    sum_right = s[r2] - s[l2 - 1] if r2 >= l2 else 0
                    dist_right = sum_right - c2 * i
                    ans = min(ans, moves + dist_left + dist_right)
                    right = mid - 1
                else:
                    left = mid + 1

        return ans
