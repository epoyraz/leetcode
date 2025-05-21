# define gcd since math.gcd may not be available
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Count existing ones
        ones = nums.count(1)
        # If all are ones, no operations needed
        if ones == n:
            return 0
        # If there is at least one 1, we can convert others by neighboring gcd operations
        if ones > 0:
            return n - ones

        # Otherwise, no initial 1s: we need to create a 1 via gcd on some subarray
        best = float('inf')
        for i in range(n):
            current = nums[i]
            for j in range(i+1, n):
                current = gcd(current, nums[j])
                if current == 1:
                    # j-i operations to yield first 1
                    best = min(best, j - i)
                    break

        # If no subarray gcd reduces to 1, impossible
        if best == float('inf'):
            return -1

        # Cost = operations to make first 1 + spread to others
        return best + (n - 1)