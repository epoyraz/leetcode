from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root):
        count = defaultdict(int)
        max_freq = [0]

        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            count[total] += 1
            max_freq[0] = max(max_freq[0], count[total])
            return total

        dfs(root)
        return [s for s in count if count[s] == max_freq[0]]
