class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        # 1) only distinct values matter (you can never take the same value twice,
        #    since after you pick v once, your sum >= v, so a second copy of v fails v > sum)
        vals = sorted(set(rewardValues))
        
        # 2) `can` as a bitset: bit s is 1 iff we can achieve a super-increasing sum = s
        can = 1  # only sum=0 is possible initially
        
        for v in vals:
            # keep only those achievable sums s < v
            mask = (1 << v) - 1
            reachable = can & mask
            # shifting them by +v gives new sums s+v
            can |= (reachable << v)
        
        # 3) the answer is the largest s for which bit s is set
        return can.bit_length() - 1
