class Solution:
    def minCameraCover(self, root):
        NOT_MONITORED = 0
        HAS_CAMERA = 1
        MONITORED = 2

        self.cameras = 0

        def dfs(node):
            if not node:
                return MONITORED

            left = dfs(node.left)
            right = dfs(node.right)

            if left == NOT_MONITORED or right == NOT_MONITORED:
                self.cameras += 1
                return HAS_CAMERA
            elif left == HAS_CAMERA or right == HAS_CAMERA:
                return MONITORED
            else:
                return NOT_MONITORED

        if dfs(root) == NOT_MONITORED:
            self.cameras += 1

        return self.cameras
