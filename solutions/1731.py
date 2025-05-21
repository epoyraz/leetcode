from collections import deque

class Solution:
    def isEvenOddTree(self, root):
        if not root:
            return True

        q = deque([root])
        level = 0

        while q:
            size = len(q)
            # For even levels we need strictly increasing odd values:
            if level % 2 == 0:
                prev = 0  # anything > 0 is fine; smallest odd is 1
            else:
                # For odd levels we need strictly decreasing even values:
                prev = float('inf')

            for _ in range(size):
                node = q.popleft()
                val = node.val

                # Check parity constraint
                if level % 2 == 0:
                    # even-indexed level: values must be odd
                    if val % 2 == 0 or val <= prev:
                        return False
                else:
                    # odd-indexed level: values must be even
                    if val % 2 == 1 or val >= prev:
                        return False

                # Update prev for strictness check
                prev = val

                # Enqueue children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return True
