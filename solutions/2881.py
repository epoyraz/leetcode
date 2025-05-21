class Solution:
    def splitWordsBySeparator(self, words, separator):
        result = []
        for word in words:
            result.extend([w for w in word.split(separator) if w])
        return result
