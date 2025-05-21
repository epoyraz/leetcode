class Solution:
    def nodesBetweenCriticalPoints(self, head):
        """
        :param head: ListNode
        :return: List[int]  # [minDistance, maxDistance]
        """
        # List to record the indices of critical points (1-based)
        critical_idxs = []
        # Initialize pointers and index
        idx = 1
        prev = head
        curr = head.next
        # Traverse until the node before tail
        while curr and curr.next:
            nxt = curr.next
            # Check if curr is a local max or min
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                critical_idxs.append(idx)
            # Move window forward
            prev, curr = curr, nxt
            idx += 1

        # If fewer than two critical points, return [-1, -1]
        if len(critical_idxs) < 2:
            return [-1, -1]

        # Compute minimum distance between consecutive critical points
        min_dist = float('inf')
        for i in range(1, len(critical_idxs)):
            dist = critical_idxs[i] - critical_idxs[i-1]
            if dist < min_dist:
                min_dist = dist
        # Maximum distance between first and last critical point
        max_dist = critical_idxs[-1] - critical_idxs[0]

        return [min_dist, max_dist]