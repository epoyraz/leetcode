class Solution:
    def sumDigitDifferences(self, nums, queries=None):
        # (ignore `queries`âwe only care about nums here)
        n = len(nums)
        # turn all numbers into strings so we can index digits
        s = list(map(str, nums))
        d = len(s[0])  # they all have the same number of digits
        
        total_pairs = n*(n-1)//2
        ans = 0
        
        # for each digit position
        for i in range(d):
            # count how many numbers have each digit 0â9 in position i
            cnt = [0]*10
            for x in s:
                cnt[ord(x[i]) - 48] += 1  # ord('0') == 48
            
            # sameâdigit pairs at this position
            same = 0
            for c in cnt:
                if c > 1:
                    same += c*(c-1)//2
            
            # the rest of the pairs differ here
            ans += total_pairs - same
        
        return ans