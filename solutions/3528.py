class Solution(object):
    def findMaximumScore(self, nums):
        n = len(nums)
        # build tree size = next power of two â¥ n
        size = 1
        while size < n:
            size <<= 1
        N = size
        # arrays for lines: m_arr[k], b_arr[k] represent y = m*x + b at node k
        m_arr = [0] * (2 * N)
        b_arr = [-10**30] * (2 * N)
        NEG_INF = -10**30

        # inline insertion of line (m_new, b_new)
        def insert_line(m_new, b_new):
            idx, l, r = 1, 0, N - 1
            while True:
                mid = (l + r) >> 1
                # if new line is better at x=mid, swap with stored
                if m_new * mid + b_new > m_arr[idx] * mid + b_arr[idx]:
                    m_arr[idx], m_new = m_new, m_arr[idx]
                    b_arr[idx], b_new = b_new, b_arr[idx]
                if l == r:
                    break
                # check left end
                if m_new * l + b_new > m_arr[idx] * l + b_arr[idx]:
                    idx <<= 1
                    r = mid
                # check right end
                elif m_new * r + b_new > m_arr[idx] * r + b_arr[idx]:
                    idx = idx * 2 + 1
                    l = mid + 1
                else:
                    break

        # inline query at point x
        def query_x(x):
            idx, l, r = 1, 0, N - 1
            res = NEG_INF
            while True:
                val = m_arr[idx] * x + b_arr[idx]
                if val > res:
                    res = val
                if l == r:
                    return res
                mid = (l + r) >> 1
                if x <= mid:
                    idx <<= 1
                    r = mid
                else:
                    idx = idx * 2 + 1
                    l = mid + 1

        # base case: dp[0] = 0, insert its line
        insert_line(nums[0], 0)
        dp = 0

        for j in range(1, n):
            # dp[j] = max_i (nums[i]*j + dp[i] - i*nums[i])
            dp = query_x(j)
            # insert line for this j
            insert_line(nums[j], dp - j * nums[j])

        return dp
