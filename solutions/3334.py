class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)
        # Sort box capacities in descending order
        capacity.sort(reverse=True)
        
        used = 0
        acc = 0
        # Pick largest boxes until we can fit all apples
        for cap in capacity:
            acc += cap
            used += 1
            if acc >= total_apples:
                return used
        
        # The problem guarantees it's always possible
        return used
