import bisect

class Solution:
    def closestNodes(self, root, queries):
        # In-order traversal to get sorted node values
        vals = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            vals.append(node.val)
            node = node.right
        
        res = []
        n = len(vals)
        for q in queries:
            # floor: largest <= q
            # bisect_right gives first index > q
            i = bisect.bisect_right(vals, q)
            floor = vals[i-1] if i > 0 else -1
            
            # ceil: smallest >= q
            # bisect_left gives first index >= q
            j = bisect.bisect_left(vals, q)
            ceil = vals[j] if j < n else -1
            
            res.append([floor, ceil])
        
        return res
