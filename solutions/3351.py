class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        # Sort in descending order
        happiness.sort(reverse=True)
        
        total = 0
        # For pick i (0-based), its value is max(happiness[i] - i, 0)
        for i in range(k):
            val = happiness[i] - i
            if val > 0:
                total += val
            else:
                # further terms will only be smaller or zero
                break
        
        return total
