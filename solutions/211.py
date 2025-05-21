class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            c = word[index]
            if c == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(index + 1, node.children[c])
        
        return dfs(0, self.root)
