class Solution(object):
    def countGoodIntegers(self, n, k):
        # Precompute factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        signatures = set()
        half = n // 2
        prefix = [0] * half

        def gen_prefix(pos):
            if pos == half:
                if n % 2 == 0:
                    # build evenâlength palindrome
                    digits = prefix + prefix[::-1]
                    x_mod = 0
                    for d in digits:
                        x_mod = (x_mod * 10 + d) % k
                    if x_mod == 0:
                        cnt = [0] * 10
                        for d in digits:
                            cnt[d] += 1
                        signatures.add(tuple(cnt))
                else:
                    # build oddâlength palindromes with every possible middle digit
                    for mid in range(10):
                        digits = prefix + [mid] + prefix[::-1]
                        x_mod = 0
                        for d in digits:
                            x_mod = (x_mod * 10 + d) % k
                        if x_mod == 0:
                            cnt = [0] * 10
                            for d in digits:
                                cnt[d] += 1
                            signatures.add(tuple(cnt))
                return

            # choose digit for prefix[pos]
            for d in range(1 if pos == 0 else 0, 10):
                prefix[pos] = d
                gen_prefix(pos + 1)

        gen_prefix(0)

        # For each valid digitâcount signature, count all nâdigit numbers
        # with that multiset (minus those with leading zero)
        ans = 0
        for cnt in signatures:
            # total permutations = n! / (Î  cnt[d]!)
            total = fact[n]
            for c in cnt:
                total //= fact[c]

            # subtract those that start with zero
            bad = 0
            if cnt[0] > 0:
                bad = fact[n - 1] // fact[cnt[0] - 1]
                for d in range(1, 10):
                    bad //= fact[cnt[d]]

            ans += total - bad

        return ans
