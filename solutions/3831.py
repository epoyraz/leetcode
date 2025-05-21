class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # result[r] = total # of subarrays whose product % k == r
        result = [0] * k
        
        # dp_prev[r] = # of subarrays ending at iâ1 with product % k == r
        dp_prev = [0] * k
        
        for a in nums:
            a_mod = a % k
            
            # dp_cur[r] = # of subarrays ending at i with product % k == r
            dp_cur = [0] * k
            
            # 1) the subarray consisting of a single element a
            dp_cur[a_mod] += 1
            
            # 2) extend each previous subarray ending at iâ1 by a
            for r in range(k):
                cnt = dp_prev[r]
                if cnt:
                    new_r = (r * a_mod) % k
                    dp_cur[new_r] += cnt
            
            # accumulate into the global result
            for r in range(k):
                result[r] += dp_cur[r]
            
            # shift dp
            dp_prev = dp_cur
        
        return result
