class Solution:
    def minFlipsMonoIncr(self, s):
        flips = 0      # flips needed to make string monotone increasing
        ones = 0       # number of 1s seen so far

        for char in s:
            if char == '1':
                ones += 1
            else:  # char == '0'
                # We can either flip this 0 to 1, or flip all previous 1s to 0s
                flips = min(flips + 1, ones)
        
        return flips
