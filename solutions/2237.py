from collections import Counter

class Solution:
    def longestPalindrome(self, words):
        count = Counter(words)
        res = 0
        center_used = False

        for word in list(count.keys()):
            rev = word[::-1]
            if word != rev:
                pairs = min(count[word], count[rev])
                res += pairs * 4
                count[word] -= pairs
                count[rev] -= pairs
            else:
                pairs = count[word] // 2
                res += pairs * 4
                count[word] -= pairs * 2

        for word in count:
            if word[0] == word[1] and count[word] > 0:
                res += 2
                break

        return res
