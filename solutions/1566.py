class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split(" ")
        for idx, w in enumerate(words, 1):
            if w.startswith(searchWord):
                return idx
        return -1
