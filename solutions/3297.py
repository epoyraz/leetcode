class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        n = len(word)
        for t in range(1, (n + k - 1) // k + 1):
            if word[k * t:] == word[:n - k * t]:
                return t
        return (n + k - 1) // k
