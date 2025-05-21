class Solution:
    def superpalindromesInRange(self, left, right):
        L, R = int(left), int(right)
        ans = 0
        limit = int(R**0.5) + 1

        # odd-length palindromic roots
        for k in range(1, 100000):
            s = str(k)
            p = int(s + s[-2::-1])   # mirror all but the last digit
            if p > limit:
                break
            sq = p * p
            if L <= sq <= R and str(sq) == str(sq)[::-1]:
                ans += 1

        # even-length palindromic roots
        for k in range(1, 100000):
            s = str(k)
            p = int(s + s[::-1])     # mirror the whole string
            if p > limit:
                break
            sq = p * p
            if L <= sq <= R and str(sq) == str(sq)[::-1]:
                ans += 1

        return ans
