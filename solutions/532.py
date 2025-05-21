class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        
        count = 0
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num in freq:
            if k == 0:
                if freq[num] > 1:
                    count += 1
            else:
                if num + k in freq:
                    count += 1
        
        return count
