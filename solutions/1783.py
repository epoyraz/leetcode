class Solution:
    def waysToMakeFair(self, nums):
        n = len(nums)
        # prefix sums of even-/odd-indexed elements
        pe = [0] * (n + 1)
        po = [0] * (n + 1)
        for i, v in enumerate(nums):
            pe[i+1] = pe[i]
            po[i+1] = po[i]
            if i & 1:
                po[i+1] += v
            else:
                pe[i+1] += v

        total_even = pe[n]
        total_odd  = po[n]
        ans = 0

        for i, v in enumerate(nums):
            left_even = pe[i]
            left_odd  = po[i]
            right_even = total_even - pe[i+1]
            right_odd  = total_odd  - po[i+1]

            new_even = left_even + right_odd
            new_odd  = left_odd  + right_even

            if new_even == new_odd:
                ans += 1

        return ans
