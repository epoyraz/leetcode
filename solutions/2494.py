class TrieNode:
    __slots__ = ('count', 'children')
    def __init__(self):
        self.count = 0
        self.children = {}

class Solution:
    def sumPrefixScores(self, words):
        # Build trie with counts
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count += 1

        # For each word, sum counts along its prefixes
        answer = []
        for w in words:
            node = root
            total = 0
            for ch in w:
                node = node.children[ch]
                total += node.count
            answer.append(total)

        return answer
