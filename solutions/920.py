from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        count = Counter(s1.split()) + Counter(s2.split())
        return [word for word in count if count[word] == 1]
