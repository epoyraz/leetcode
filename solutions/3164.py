class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = []
        ans = []
        consec = 0
        for x in nums:
            if x == -1:
                consec += 1
                if consec <= len(seen):
                    ans.append(seen[consec - 1])
                else:
                    ans.append(-1)
            else:
                # prepend positive integer
                seen.insert(0, x)
                consec = 0
        return ans
