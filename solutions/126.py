class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # If endWord is not in wordList, no valid transformation sequence exists
        if endWord not in wordList:
            return []
        
        # Convert wordList to a set for O(1) lookups
        word_set = set(wordList)
        
        # Store the level at which each word is first visited
        level_map = {beginWord: 0}
        
        # Keep track of all possible parents for each word
        parents = collections.defaultdict(list)
        
        # BFS to find all words and their minimum levels
        queue = collections.deque([beginWord])
        found = False
        level = 0
        
        # Only process until we find endWord (minimum level)
        while queue and not found:
            size = len(queue)
            level += 1
            
            # For words being visited at current level
            curr_level_visited = set()
            
            for _ in range(size):
                word = queue.popleft()
                
                # Try changing each character and check if it's a valid next word
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        
                        # Skip if it's the same word or not in our word set
                        if next_word == word or next_word not in word_set:
                            continue
                        
                        # If we haven't seen this word before, add to queue
                        if next_word not in level_map:
                            level_map[next_word] = level
                            curr_level_visited.add(next_word)
                            queue.append(next_word)
                            parents[next_word].append(word)
                        # If we've seen this word at the current level, update its parents
                        elif level_map[next_word] == level:
                            parents[next_word].append(word)
                        
                        # Check if we've reached endWord
                        if next_word == endWord:
                            found = True
            
            # Remove words visited at current level to avoid cycles
            for word in curr_level_visited:
                if word in word_set:
                    word_set.remove(word)
        
        # If endWord is not found, return empty list
        if endWord not in level_map:
            return []
        
        # Use DFS to build all paths from endWord back to beginWord
        result = []
        
        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            
            for parent in parents[word]:
                dfs(parent, path + [parent])
        
        dfs(endWord, [endWord])
        return result