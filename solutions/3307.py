class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Base sum of original values
        base_sum = sum(nums)
        
        # Î[i] = gain if we flip node i once (xor k)
        delta = [(nums[i] ^ k) - nums[i] for i in range(len(nums))]
        
        # All strictly positive gains
        positives = [d for d in delta if d > 0]
        G = sum(positives)
        
        # If we have an even number of positives, we can take them all
        if len(positives) % 2 == 0:
            best_gain = G
        else:
            # Otherwise we must sacrifice the smaller of:
            # 1) dropping the smallest positive Î
            min_pos = min(positives)
            # 2) adding the least-negative Î (i.e. the maximum among non-positives)
            nonpos = [d for d in delta if d <= 0]
            if nonpos:
                max_neg = nonpos[0]
                for d in nonpos:
                    if d > max_neg:
                        max_neg = d
                cost_add_neg = -max_neg
            else:
                # no non-positive to add, force dropping
                cost_add_neg = float('inf')
            
            loss = min(min_pos, cost_add_neg)
            best_gain = G - loss
        
        return base_sum + best_gain
