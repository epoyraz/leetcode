class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        # next_pos[b] = the smallest index >= i where bit b is set
        # Initialize to n (meaning "not seen")
        next_pos = [n] * 32
        answer = [1] * n

        # Process from right to left
        for i in range(n - 1, -1, -1):
            x = nums[i]
            # Update next_pos for bits set in nums[i]
            b = 0
            while x:
                if x & 1:
                    next_pos[b] = i
                x >>= 1
                b += 1

            # Determine the farthest needed index to cover all bits
            farthest = i
            for pos in next_pos:
                if pos < n and pos > farthest:
                    farthest = pos

            answer[i] = farthest - i + 1

        return answer
