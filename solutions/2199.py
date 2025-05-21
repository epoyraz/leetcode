class Solution:
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        first_color = colors[0]
        last_color = colors[-1]
        
        # Furthest from the start that differs from colors[0]
        max_from_start = 0
        for j in range(n - 1, -1, -1):
            if colors[j] != first_color:
                max_from_start = j
                break
        
        # Furthest from the end that differs from colors[-1]
        min_from_end = n - 1
        for i in range(n):
            if colors[i] != last_color:
                min_from_end = i
                break
        
        return max(max_from_start, (n - 1) - min_from_end)
