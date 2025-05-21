class Solution(object):
    def countPairs(self, nums, low, high):
        # determine bit length needed
        bitlen = max(high.bit_length(), max(nums).bit_length())
        # maximum number of trie nodes
        max_nodes = (len(nums) + 1) * (bitlen + 1)
        # children[b][i] = next node index from node i on bit b (0 or 1)
        children = [[-1] * max_nodes for _ in range(2)]
        # counts[i] = number of values inserted that pass through node i
        counts = [0] * max_nodes
        # next available node index
        node_count = [1]  # use list for mutability in nested scope

        def add(x):
            node = 0
            for i in range(bitlen - 1, -1, -1):
                b = (x >> i) & 1
                nxt = children[b][node]
                if nxt == -1:
                    nxt = node_count[0]
                    children[b][node] = nxt
                    node_count[0] += 1
                node = nxt
                counts[node] += 1

        def query(x, limit):
            if limit < 0:
                return 0
            res = 0
            node = 0
            for i in range(bitlen - 1, -1, -1):
                if node == -1:
                    break
                b = (x >> i) & 1
                l = (limit >> i) & 1
                if l:
                    # add all in branch where x^y bit = 0 => y bit = b
                    child = children[b][node]
                    if child != -1:
                        res += counts[child]
                    # then go to branch where x^y bit = 1 => y bit = 1-b
                    node = children[1 - b][node]
                else:
                    # must go to branch where x^y bit = 0 => y bit = b
                    node = children[b][node]
            if node != -1:
                res += counts[node]
            return res

        ans = 0
        for x in nums:
            ans += query(x, high) - query(x, low - 1)
            add(x)
        return ans
