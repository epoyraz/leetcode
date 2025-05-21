class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Track current color of each ball (sparse, since labels can be large)
        ball_color = {}
        # Count how many balls have each color
        color_count = {}
        # Number of distinct colors currently in use
        distinct = 0
        
        result = []
        for x, y in queries:
            # Remove old color of ball x, if any
            old = ball_color.get(x)
            if old is not None:
                color_count[old] -= 1
                if color_count[old] == 0:
                    # that color is no longer present
                    distinct -= 1
            
            # Assign new color y to ball x
            ball_color[x] = y
            if color_count.get(y, 0) == 0:
                # this color was not in use before
                distinct += 1
            color_count[y] = color_count.get(y, 0) + 1
            
            # Record the current number of distinct colors
            result.append(distinct)
        
        return result