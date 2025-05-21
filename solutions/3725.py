class Solution(object):
    def minMaxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k:    int
        :rtype:     int
        """
        n = len(nums)

        # 1) prev_less (strict) & next_less_or_equal
        prev_less = [-1]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        next_less = [n]*n
        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                next_less[stack[-1]] = i
                stack.pop()
            stack.append(i)

        # 2) prev_greater (strict) & next_greater_or_equal
        prev_greater = [-1]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            prev_greater[i] = stack[-1] if stack else -1
            stack.append(i)

        next_greater = [n]*n
        stack = []
        for i in range(n):
            while stack and nums[i] >= nums[stack[-1]]:
                next_greater[stack[-1]] = i
                stack.pop()
            stack.append(i)

        # Helper: count all subarrays of length â¤ k, containing i,
        # whose min (or max) is at i given bounds L < l <= i <= r < R.
        def count_extremes(i, L, R):
            # l in [A..B] = [L+1 .. i], but also need l+k-1 >= i so
            # l >= i-k+1.  So l from l_start..B where
            A = L + 1
            B = i
            l_start = max(A, i - k + 1)

            # Split at l â¤ R-k  and l > R-k
            t = min(B, R - k)
            # 1) l in [l_start..t], count(l) = (l+k-1) - i + 1 = l + k - i
            if t >= l_start:
                n1 = t - l_start + 1
                # sum of l from l_start to t = n1*(l_start + t)//2
                sum_l = n1 * (l_start + t) // 2
                sum1 = sum_l + n1 * (k - i)
            else:
                sum1 = 0

            # 2) l in [max(l_start, R-k+1)..B], count(l) = (R-1)-i+1 = R-i
            l2_start = max(l_start, R - k + 1)
            if l2_start <= B:
                n2 = B - l2_start + 1
                sum2 = n2 * (R - i)
            else:
                sum2 = 0

            return sum1 + sum2

        total = 0
        for i in range(n):
            cnt_min = count_extremes(i, prev_less[i],  next_less[i])
            cnt_max = count_extremes(i, prev_greater[i], next_greater[i])
            total += nums[i] * (cnt_min + cnt_max)

        return total
