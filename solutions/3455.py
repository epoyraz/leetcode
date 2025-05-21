class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count occurrences of each lowercase letter
        cnt = [0]*26
        for ch in s:
            cnt[ord(ch)-97] += 1
        
        # Compute final leftover
        ans = 0
        for c in cnt:
            if c == 0:
                continue
            # if odd count -> 1 remains; if even -> 2 remain
            ans += 1 if (c % 2) else 2
        
        return ans
