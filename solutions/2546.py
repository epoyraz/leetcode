class Solution:
    def subarrayGCD(self, nums, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        ans = 0
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                # If gcd drops below k or isn't a multiple of k, we can stop extending
                if g < k or g % k != 0:
                    break
                if g == k:
                    ans += 1
        return ans
