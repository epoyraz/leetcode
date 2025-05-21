from collections import deque

class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.deque = deque()
        
        # Level order traversal to find incomplete nodes
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val):
        node = self.deque[0]
        new_node = TreeNode(val)
        
        if not node.left:
            node.left = new_node
        else:
            node.right = new_node
            self.deque.popleft()
        
        self.deque.append(new_node)
        return node.val

    def get_root(self):
        return self.root
