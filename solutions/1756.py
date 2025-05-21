class Solution:
    def minimumDeletions(self, s):
        a_remain = s.count('a')
        b_count = 0
        ans = float('inf')
        
        for ch in s:
            # deletions = b's to left + a's to right
            ans = min(ans, b_count + a_remain)
            if ch == 'a':
                a_remain -= 1
            else:
                b_count += 1
        
        # split after the last character
        ans = min(ans, b_count + a_remain)
        return ans
