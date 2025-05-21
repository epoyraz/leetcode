class Solution(object):
    def leastBricks(self, wall):
        from collections import Counter
        edge_counts = Counter()
        for row in wall:
            cum_width = 0
            # exclude the last brick to avoid the right edge of the wall
            for width in row[:-1]:
                cum_width += width
                edge_counts[cum_width] += 1
        # if there are no internal edges, we must cross every row
        if not edge_counts:
            return len(wall)
        # draw the line through the position with the most edges
        max_edges = max(edge_counts.values())
        return len(wall) - max_edges
