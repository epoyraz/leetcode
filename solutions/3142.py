class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)

        def hamming(a, b):
            # Assumes len(a) == len(b)
            return sum(x != y for x, y in zip(a, b))

        # dp[i]: length of longest valid subsequence ending at i
        dp = [1] * n
        prev = [-1] * n

        best_i = 0
        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i] \
                   and len(words[j]) == len(words[i]) \
                   and hamming(words[j], words[i]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[best_i]:
                best_i = i

        # Reconstruct subsequence
        seq = []
        cur = best_i
        while cur != -1:
            seq.append(words[cur])
            cur = prev[cur]
        return seq[::-1]
