from collections import Counter

class Solution:
    def wordSubsets(self, words1, words2):
        def count(word):
            return Counter(word)

        # Compute the maximum required count for each character from words2
        max_count = Counter()
        for b in words2:
            b_count = count(b)
            for char in b_count:
                max_count[char] = max(max_count[char], b_count[char])

        res = []
        for a in words1:
            a_count = count(a)
            if all(a_count[c] >= max_count[c] for c in max_count):
                res.append(a)

        return res
