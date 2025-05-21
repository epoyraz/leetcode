class Solution(object):
    def vowelStrings(self, words, queries):
        vowels = set('aeiou')
        n = len(words)
        prefix = [0] * (n + 1)

        for i in range(n):
            w = words[i]
            if w[0] in vowels and w[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]

        res = []
        for l, r in queries:
            res.append(prefix[r + 1] - prefix[l])
        return res
