class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        m, n = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            c = board[i][j]
            if c not in node.children:
                return
            node = node.children[c]
            if node.word:
                res.append(node.word)
                node.word = None
            
            board[i][j] = '#'
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, node)
            board[i][j] = c
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return res
