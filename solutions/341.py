class NestedIterator(object):
    def __init__(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self._flatten(nestedList)
        self.stack.reverse()

    def _flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.stack.append(item.getInteger())
            else:
                self._flatten(item.getList())

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)
