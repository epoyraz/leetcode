class Solution:
    def numberOfUniqueGoodSubsequences(self, binary):
        mod = 10**9 + 7
        ends_with_0 = 0
        ends_with_1 = 0
        has_zero = False

        for c in binary:
            if c == '0':
                # Append '0' to all subsequences that end with '1'
                ends_with_0 = (ends_with_0 + ends_with_1) % mod
                has_zero = True
            else:
                # Append '1' to all existing subsequences (ends_with_0 + ends_with_1)
                # and also start a new subsequence "1"
                ends_with_1 = (ends_with_1 + ends_with_0 + 1) % mod

        # Total = all non-empty subsequences starting with '1' (those ending in '0' or '1')
        #      + the single "0" subsequence if any '0' exists
        return (ends_with_1 + ends_with_0 + (1 if has_zero else 0)) % mod
