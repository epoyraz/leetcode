class Solution:
    def minimizeConcatenatedLength(self, words):
        n = len(words)
        memo = {}

        def dp(i, first, last):
            key = (i, first, last)
            if key in memo:
                return memo[key]
            if i == n:
                return 0

            word = words[i]
            wlen = len(word)
            wf, wl = word[0], word[-1]

            # join(str + word)
            overlap1 = 1 if last == wf else 0
            cost1 = wlen - overlap1 + dp(i + 1, first, wl)

            # join(word + str)
            overlap2 = 1 if wl == first else 0
            cost2 = wlen - overlap2 + dp(i + 1, wf, last)

            memo[key] = min(cost1, cost2)
            return memo[key]

        first_word = words[0]
        return len(first_word) + dp(1, first_word[0], first_word[-1])
