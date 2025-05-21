class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        if original is None:
            return None
        if original == target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        return self.getTargetCopy(original.right, cloned.right, target)
