class Solution:
    def getSmallestString(self, n, k):
        # Start with all 'a's: total value = n
        res = ['a'] * n
        rem = k - n  # remaining value to distribute

        # Fill from the end with as large letters as needed
        i = n - 1
        while rem > 0:
            add = min(25, rem)  # can increase 'a' by up to 25 to reach 'z'
            res[i] = chr(ord('a') + add)
            rem -= add
            i -= 1

        return "".join(res)
