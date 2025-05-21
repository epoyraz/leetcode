from collections import Counter

class Solution:
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        c1 = Counter(words1)
        c2 = Counter(words2)
        
        count = 0
        # Only strings appearing in both can qualify
        for word in c1:
            if c1[word] == 1 and c2.get(word, 0) == 1:
                count += 1
        
        return count
