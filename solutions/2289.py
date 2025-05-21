from collections import Counter

class Solution:
    def minimumOperations(self, nums):
        even = Counter(nums[::2])
        odd = Counter(nums[1::2])

        even_items = even.most_common(2) + [(0, 0)]
        odd_items = odd.most_common(2) + [(0, 0)]

        if even_items[0][0] != odd_items[0][0]:
            return len(nums) - even_items[0][1] - odd_items[0][1]
        return min(
            len(nums) - even_items[0][1] - odd_items[1][1],
            len(nums) - even_items[1][1] - odd_items[0][1]
        )
