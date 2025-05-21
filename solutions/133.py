class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # Dictionary to map original nodes to their clones
        cloned = {}
        
        def dfs(original):
            # If we've already cloned this node, return its clone
            if original in cloned:
                return cloned[original]
            
            # Create clone of the current node
            clone = Node(original.val)
            
            # Add to dictionary before exploring neighbors (to handle cycles)
            cloned[original] = clone
            
            # Clone and connect all neighbors
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)