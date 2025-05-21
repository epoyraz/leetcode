class Solution(object):
    def longestBeautifulSubstring(self, word):
        idx = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        n = len(word)
        if n < 5:
            return 0
        start = 0
        prev = idx[word[0]]
        distinct = 1
        ans = 0
        for i in range(1, n):
            curr = idx[word[i]]
            if curr < prev:
                start = i
                distinct = 1
            else:
                if curr > prev:
                    distinct += 1
                if distinct == 5:
                    ans = max(ans, i - start + 1)
            prev = curr
        return ans
