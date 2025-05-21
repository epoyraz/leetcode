class Solution:
    def maximumNumberOfStringPairs(self, words):
        seen = set()
        count = 0
        
        for word in words:
            rev = word[::-1]
            if rev in seen:
                count += 1
            seen.add(word)
        
        return count
