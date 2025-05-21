class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        buckets_min = [float('inf')] * bucket_count
        buckets_max = [float('-inf')] * bucket_count
        
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)
        
        max_gap = 0
        prev_max = min_val
        for i in range(bucket_count):
            if buckets_min[i] == float('inf'):
                continue
            max_gap = max(max_gap, buckets_min[i] - prev_max)
            prev_max = buckets_max[i]
        
        return max_gap
