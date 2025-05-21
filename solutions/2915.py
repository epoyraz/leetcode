class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        
        count = defaultdict(int)
        # prefix sum modulo counts
        # P[0] = 0
        count[0] = 1
        
        prefix = 0
        ans = 0
        
        for x in nums:
            # A[i] = 1 if x % modulo == k else 0
            if x % modulo == k:
                prefix += 1
            # current prefix modulo
            pm = prefix % modulo
            # we want previous prefix modulo â¡ pm - k (mod modulo)
            need = (pm - k) % modulo
            ans += count.get(need, 0)
            # record this prefix modulo
            count[pm] += 1
        
        return ans
