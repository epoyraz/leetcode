class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        res = []

        def canForm(word):
            if not word: return False
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        if j == 0 and i == len(word):
                            continue  # skip if the whole word matches
                        dp[i] = True
                        break
            return dp[len(word)]

        for word in words:
            word_set.remove(word)
            if canForm(word):
                res.append(word)
            word_set.add(word)

        return res
