class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # If endWord is not in wordList, no valid transformation sequence exists
        if endWord not in wordList:
            return 0
        
        # Convert wordList to a set for O(1) lookups
        word_set = set(wordList)
        
        # Initialize queue with beginWord and the current sequence length
        queue = [(beginWord, 1)]
        visited = set([beginWord])
        
        # BFS to find the shortest path
        while queue:
            current_word, path_length = queue.pop(0)
            
            # Try changing each character position
            for i in range(len(current_word)):
                # Try each possible letter
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Create new word with the character at position i changed
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    # If we found the endWord, return the path length + 1
                    if next_word == endWord:
                        return path_length + 1
                    
                    # If the word is in our wordList and hasn't been visited yet
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, path_length + 1))
                        
                        # Optional optimization: remove from word_set to avoid checking again
                        word_set.remove(next_word)
        
        # No path found
        return 0