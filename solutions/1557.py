class Solution(object):
    def hasAllCodes(self, s, k):
        n = len(s)
        # If there are fewer than k bits, can't have any k-length code
        if n < k:
            return False
        total = 1 << k
        # To contain all k-length binary codes, s must have at least total substrings of length k
        # i.e., n - k + 1 >= total  =>  n >= total + k - 1
        if n < total + k - 1:
            return False

        mask = total - 1
        seen = bytearray(total)
        count = 0
        val = 0
        # build initial value for first k bits
        for i in range(k):
            val = ((val << 1) & mask) | (ord(s[i]) - ord('0'))
        seen[val] = 1
        count = 1

        # slide the window
        for i in range(k, n):
            # add new bit, drop oldest by masking
            val = ((val << 1) & mask) | (ord(s[i]) - ord('0'))
            if not seen[val]:
                seen[val] = 1
                count += 1
                if count == total:
                    return True

        return count == total
