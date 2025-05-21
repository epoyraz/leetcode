class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = words[i], words[j]
                if len(a) <= len(b) and b.startswith(a) and b.endswith(a):
                    count += 1
        return count
