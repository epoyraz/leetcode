class Solution:
    def countBeautifulPairs(self, nums):
        def first_digit(x):
            while x >= 10:
                x //= 10
            return x

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = 0
        n = len(nums)
        for i in range(n):
            fi = first_digit(nums[i])
            for j in range(i + 1, n):
                lj = nums[j] % 10
                if gcd(fi, lj) == 1:
                    count += 1
        return count
