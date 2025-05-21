class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        # prev holds pairs (and_value, count) for subarrays ending at previous index
        prev = []
        for x in nums:
            curr = [(x, 1)]
            # extend previous subarrays by x
            for val, cnt in prev:
                new_val = val & x
                if curr[-1][0] == new_val:
                    # merge counts if same AND value
                    curr[-1] = (new_val, curr[-1][1] + cnt)
                else:
                    curr.append((new_val, cnt))
            # count those ending here with AND == k
            for val, cnt in curr:
                if val == k:
                    res += cnt
            prev = curr
        return res
