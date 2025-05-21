class Solution(object):
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict
        count = defaultdict(int)
        res = []
        
        def serialize(node):
            if not node:
                return "#"
            serial = "{},{},{}".format(node.val, serialize(node.left), serialize(node.right))
            count[serial] += 1
            if count[serial] == 2:
                res.append(node)
            return serial
        
        serialize(root)
        return res
