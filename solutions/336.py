class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_to_index = {word: i for i, word in enumerate(words)}
        res = []
        
        def is_palindrome(word):
            return word == word[::-1]
        
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                prefix, suffix = word[:j], word[j:]
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back in word_to_index and word_to_index[back] != i:
                        res.append([word_to_index[back], i])
                if j != len(word) and is_palindrome(suffix):
                    front = prefix[::-1]
                    if front in word_to_index and word_to_index[front] != i:
                        res.append([i, word_to_index[front]])
        
        return res
