class BinaryTrie:
    __slots__ = ('child', 'count')
    def __init__(self):
        self.child = [None, None]
        self.count = 0
        
class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()
        n = len(nums)

        # Trie for 20-bit numbers (nums[i] <= 2^20-1)
        root = BinaryTrie()

        def insert(x):
            node = root
            node.count += 1
            for b in reversed(range(20)):  # bits 19..0
                bit = (x >> b) & 1
                if node.child[bit] is None:
                    node.child[bit] = BinaryTrie()
                node = node.child[bit]
                node.count += 1

        def remove(x):
            node = root
            node.count -= 1
            for b in reversed(range(20)):
                bit = (x >> b) & 1
                nxt = node.child[bit]
                node = nxt
                node.count -= 1

        def max_xor_with(x):
            node = root
            res = 0
            for b in reversed(range(20)):
                bit = (x >> b) & 1
                toggled = bit ^ 1
                # prefer opposite bit if available
                child = node.child[toggled]
                if child is not None and child.count > 0:
                    res |= (1 << b)
                    node = child
                else:
                    node = node.child[bit]
            return res

        best = 0
        l = 0
        r = 0

        for i, x in enumerate(nums):
            # expand r while nums[r] <= 2*x
            while r < n and nums[r] <= 2 * x:
                insert(nums[r])
                r += 1
            # shrink l while nums[l] < ceil(x/2)
            half = (x + 1) // 2
            while l < n and nums[l] < half:
                remove(nums[l])
                l += 1

            # query max xor with x in current window
            # window guaranteed to contain x itself
            curr = max_xor_with(x)
            if curr > best:
                best = curr

        return best