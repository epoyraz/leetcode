class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        arr = []
        while nums:
            # Alice removes min
            alice = nums.pop(0)
            # Bob removes new min
            bob = nums.pop(0)
            # Bob appends first, then Alice
            arr.append(bob)
            arr.append(alice)
        return arr
