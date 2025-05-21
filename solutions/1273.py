from bisect import bisect_right

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def f(s):
            return s.count(min(s))

        word_freqs = sorted(f(w) for w in words)
        result = []

        for q in queries:
            fq = f(q)
            # Find how many word frequencies are > fq
            count = len(word_freqs) - bisect_right(word_freqs, fq)
            result.append(count)

        return result
