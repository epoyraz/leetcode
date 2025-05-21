import math

class Solution:
    def subarrayLCM(self, nums, k):
        # helper gcd in case math.gcd isn't available
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        ans = 0

        for i in range(n):
            cur_lcm = 1
            for j in range(i, n):
                x = nums[j]
                # if x doesn't divide k, no subarray from i.. can reach LCM = k
                if k % x != 0:
                    break
                # update LCM safely using custom gcd
                cur_lcm = cur_lcm * x // gcd(cur_lcm, x)
                # if we've exceeded k, we can stop (since x|k and cur_lcm|k, won't exceed)
                # but as x divides k, cur_lcm will always divide k, so no need to check >k
                if cur_lcm == k:
                    ans += 1
            # next i
        return ans