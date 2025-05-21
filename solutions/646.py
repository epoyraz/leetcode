class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        curr = float('-inf')
        count = 0
        
        for pair in pairs:
            if curr < pair[0]:
                curr = pair[1]
                count += 1
        
        return count
