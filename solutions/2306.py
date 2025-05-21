class Solution(object):
    def createBinaryTree(self, descriptions):
        nodes   = {}          # value -> TreeNode
        has_par = set()       # every value that ever appears as a child
        
        for par, child, isLeft in descriptions:
            if par   not in nodes: nodes[par]   = TreeNode(par)
            if child not in nodes: nodes[child] = TreeNode(child)

            if isLeft:
                nodes[par].left  = nodes[child]
            else:
                nodes[par].right = nodes[child]

            has_par.add(child)

        # root is the node that never appeared as a child
        for val in nodes:
            if val not in has_par:
                return nodes[val]