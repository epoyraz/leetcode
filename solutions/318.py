class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        masks = [0] * n
        for i in range(n):
            for c in words[i]:
                masks[i] |= 1 << (ord(c) - ord('a'))
        
        max_product = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product
