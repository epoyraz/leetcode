class Solution:
    def sumImbalanceNumbers(self, nums):
        n = len(nums)
        total = 0
        
        for i in range(n):
            seen = set()
            cur = 0
            seen.add(nums[i])
            for j in range(i + 1, n):
                x = nums[j]
                if x not in seen:
                    if x - 1 in seen and x + 1 in seen:
                        cur -= 1
                    elif x - 1 not in seen and x + 1 not in seen:
                        cur += 1
                    # else: exactly one neighbor is in â imbalance doesn't change
                seen.add(x)
                total += cur
        
        return total
