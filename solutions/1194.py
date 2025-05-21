class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        level = 0
        while (1 << level) <= label:
            level += 1

        while label >= 1:
            res.append(label)
            level -= 1
            # Find the range of the current level
            start = 1 << level
            end = (1 << (level + 1)) - 1
            # Move to the parent in normal binary tree,
            # then reverse it if needed
            label = (start + end - label) // 2

        return res[::-1]
