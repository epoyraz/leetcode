class Solution:
    def maxProduct(self, s):
        n = len(s)
        palins = {}

        # Step 1: collect all palindromic subsequences with their bitmask
        for mask in range(1, 1 << n):
            subseq = []
            for i in range(n):
                if (mask >> i) & 1:
                    subseq.append(s[i])
            if subseq == subseq[::-1]:
                palins[mask] = len(subseq)

        # Step 2: try all disjoint pairs
        max_product = 0
        keys = list(palins.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i] & keys[j] == 0:
                    max_product = max(max_product, palins[keys[i]] * palins[keys[j]])

        return max_product
