class Solution:
    def minOperations(self, nums1, nums2):
        from collections import Counter

        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0

        # Ensure nums1 has the larger sum
        if s1 < s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        # Build frequency of possible changes (1â6 = +5, 6â1 = -5)
        diff = s1 - s2
        changes = [0] * 6

        for num in nums1:
            changes[num - 1] += 1  # max decrease: num - 1
        for num in nums2:
            changes[6 - num] += 1  # max increase: 6 - num

        ops = 0
        for i in range(5, 0, -1):  # i is the gain from a change
            while changes[i] > 0 and diff > 0:
                take = min(changes[i], (diff + i - 1) // i)
                diff -= take * i
                ops += take
                changes[i] -= take

        return ops if diff <= 0 else -1
