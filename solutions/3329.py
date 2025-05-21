class TrieNode(object):
    def __init__(self):
        self.children = {}

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        def insert(trie, num_str):
            node = trie
            for ch in num_str:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

        def longest_match(trie, num_str):
            node = trie
            lcp = 0
            for ch in num_str:
                if ch in node.children:
                    lcp += 1
                    node = node.children[ch]
                else:
                    break
            return lcp

        trie = TrieNode()
        for num in arr2:
            insert(trie, str(num))

        max_len = 0
        for num in arr1:
            max_len = max(max_len, longest_match(trie, str(num)))
        return max_len
