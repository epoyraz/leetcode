class Solution(object):
    def findPrefixScore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        max_val = float('-inf')
        total = 0

        for num in nums:
            max_val = max(max_val, num)
            converted = num + max_val
            total += converted
            ans.append(total)

        return ans
