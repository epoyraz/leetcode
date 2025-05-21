# Below is the interface for Iterator, which is already defined.
# You should not implement it, or speculate about its implementation.
class Iterator(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.index = 0

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.nums)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            val = self.nums[self.index]
            self.index += 1
            return val
        else:
            return None

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._peek = None
        if self.iterator.hasNext():
            self._peek = self.iterator.next()

    def peek(self):
        """
        :rtype: int
        """
        return self._peek

    def next(self):
        """
        :rtype: int
        """
        val = self._peek
        if self.iterator.hasNext():
            self._peek = self.iterator.next()
        else:
            self._peek = None
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._peek is not None
