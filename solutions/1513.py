class Solution(object):
    def findGoodStrings(self, n, s1, s2, evil):
        MOD = 10**9 + 7
        ALPHABET = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        # Build KMP failure function for evil
        def build_kmp(pattern):
            fail = [0] * len(pattern)
            for i in range(1, len(pattern)):
                j = fail[i - 1]
                while j > 0 and pattern[i] != pattern[j]:
                    j = fail[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                fail[i] = j
            return fail

        kmp = build_kmp(evil)
        memo = {}

        def dp(pos, matched, is_prefix_s1, is_prefix_s2):
            key = (pos, matched, is_prefix_s1, is_prefix_s2)
            if key in memo:
                return memo[key]
            if matched == len(evil):
                return 0
            if pos == n:
                return 1

            res = 0
            start = s1[pos] if is_prefix_s1 else 'a'
            end = s2[pos] if is_prefix_s2 else 'z'

            for c in ALPHABET:
                if start <= c <= end:
                    new_matched = matched
                    while new_matched > 0 and c != evil[new_matched]:
                        new_matched = kmp[new_matched - 1]
                    if c == evil[new_matched]:
                        new_matched += 1

                    res += dp(
                        pos + 1,
                        new_matched,
                        is_prefix_s1 and c == s1[pos],
                        is_prefix_s2 and c == s2[pos]
                    )
                    res %= MOD

            memo[key] = res
            return res

        return dp(0, 0, True, True)
