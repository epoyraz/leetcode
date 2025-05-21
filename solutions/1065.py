class Solution:
    def queryString(self, s, n):
        seen = set()
        max_len = min(len(s), n.bit_length())

        for length in range(1, max_len + 1):
            for i in range(len(s) - length + 1):
                num = int(s[i:i+length], 2)
                if 1 <= num <= n:
                    seen.add(num)
            # Early exit if we've found all numbers
            if len(seen) == n:
                return True

        return len(seen) == n
