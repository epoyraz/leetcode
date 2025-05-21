class FrontMiddleBackQueue:
    def __init__(self):
        self.left = []
        self.right = []

    def _rebalance(self):
        total = len(self.left) + len(self.right)
        target = total // 2
        # left should have floor(total/2) elements
        while len(self.left) > target:
            # move last of left to front of right
            self.right.insert(0, self.left.pop())
        while len(self.left) < target:
            # move first of right to end of left
            self.left.append(self.right.pop(0))

    def pushFront(self, val):
        self.left.insert(0, val)
        self._rebalance()

    def pushMiddle(self, val):
        # frontmost middle is end of left
        self.left.append(val)
        self._rebalance()

    def pushBack(self, val):
        self.right.append(val)
        self._rebalance()

    def popFront(self):
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.pop(0)
        else:
            val = self.right.pop(0)
        self._rebalance()
        return val

    def popMiddle(self):
        if not self.left and not self.right:
            return -1
        total = len(self.left) + len(self.right)
        mid = (total - 1) // 2
        if mid < len(self.left):
            val = self.left.pop(mid)
        else:
            val = self.right.pop(mid - len(self.left))
        self._rebalance()
        return val

    def popBack(self):
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._rebalance()
        return val
