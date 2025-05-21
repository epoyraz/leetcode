class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        words1 = sentence1.split()
        words2 = sentence2.split()
        # ensure words1 is the shorter
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        n1, n2 = len(words1), len(words2)
        # match prefix
        i = 0
        while i < n1 and words1[i] == words2[i]:
            i += 1
        # match suffix
        j = 0
        while j < n1 - i and words1[-1 - j] == words2[-1 - j]:
            j += 1
        return i + j == n1
