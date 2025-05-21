class Solution:
    def tupleSameProduct(self, nums):
        from collections import defaultdict

        prod_count = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                prod_count[prod] += 1

        res = 0
        for count in prod_count.values():
            if count > 1:
                res += count * (count - 1) * 4  # 4 permutations per pair
        return res
