class Solution:
    def sumEvenGrandparent(self, root):
        stack = [(root, None, None)]
        total = 0
        while stack:
            node, parent, grand = stack.pop()
            if not node:
                continue
            if grand and grand.val % 2 == 0:
                total += node.val
            stack.append((node.left, node, parent))
            stack.append((node.right, node, parent))
        return total
