import heapq

class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums.sort()
        # queries_with_idx = [(mi, xi, original_index), ...] sorted by mi
        queries_with_idx = sorted(
            [(mi, xi, i) for i, (xi, mi) in enumerate(queries)]
        )
        
        # We'll build a bitwise trie; each node has children[0] and children[1].
        children = [[-1, -1]]
        node_count = [1]   # store as list so inner functions can update
        
        def trie_insert(x):
            node = 0
            # from bit 30 down to bit 0
            for b in range(30, -1, -1):
                bit = (x >> b) & 1
                nxt = children[node][bit]
                if nxt == -1:
                    nxt = node_count[0]
                    children[node][bit] = nxt
                    children.append([-1, -1])
                    node_count[0] += 1
                node = nxt
        
        def trie_max_xor(x):
            node = 0
            res = 0
            for b in range(30, -1, -1):
                bit = (x >> b) & 1
                want = 1 - bit
                if children[node][want] != -1:
                    res |= (1 << b)
                    node = children[node][want]
                else:
                    node = children[node][bit]
            return res
        
        res = [-1] * len(queries)
        p = 0  # pointer into nums
        
        for mi, xi, qi in queries_with_idx:
            # insert all nums[p] <= mi into the trie
            while p < len(nums) and nums[p] <= mi:
                trie_insert(nums[p])
                p += 1
            # if we inserted nothing yet, answer is -1
            if p == 0:
                res[qi] = -1
            else:
                res[qi] = trie_max_xor(xi)
        
        return res
