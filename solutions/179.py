from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
