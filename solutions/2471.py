class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        n = len(garbage)
        # prefix[i] = time to travel from house 0 to house i
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + travel[i - 1]

        # Track the last house index where each type appears
        last = {'M': -1, 'P': -1, 'G': -1}
        total_pickup = 0

        for i, s in enumerate(garbage):
            total_pickup += len(s)
            for ch in ('M', 'P', 'G'):
                if ch in s:
                    last[ch] = i

        # Sum up travel time for each truck to its last needed house
        total_time = total_pickup
        for ch in ('M', 'P', 'G'):
            idx = last[ch]
            if idx != -1:
                total_time += prefix[idx]

        return total_time
