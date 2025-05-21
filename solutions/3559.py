class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False  # indicates a valid prefix

class Solution(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        root = TrieNode()
        
        # insert all prefixes of each word into trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.end = True  # mark every prefix as valid

        n = len(target)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            node = root
            for j in range(i, n):
                c = target[j]
                if c not in node.children:
                    break
                node = node.children[c]
                if node.end:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)

        return dp[n] if dp[n] != INF else -1
