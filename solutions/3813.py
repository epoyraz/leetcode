class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        from collections import Counter

        # 1) Build halfâcounts and optional middle character
        full = Counter(s)
        mid = ""
        cnt = {}
        for ch, freq in full.items():
            if freq % 2:
                mid = ch
            cnt[ch] = freq // 2

        m = sum(cnt.values())
        if m == 0:
            return s if k == 1 else ""

        # capped binomial C(n, r) but never exceeding cap
        def capped_comb(n, r, cap):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
                if res > cap:
                    return cap
            return res

        # count permutations of the multiset 'cnt', but earlyâexit at cap
        def count_perms(cnt, cap):
            rem = sum(cnt.values())
            total = 1
            for ch in sorted(cnt):
                c = cnt[ch]
                if c == 0:
                    continue
                ways = capped_comb(rem, c, cap)
                total *= ways
                if total >= cap:
                    return cap
                rem -= c
            return total

        # 2) Greedily build the first half
        half = []
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for _ in range(m):
            for c in letters:
                if cnt.get(c, 0) == 0:
                    continue
                cnt[c] -= 1
                num = count_perms(cnt, k)
                if num >= k:
                    half.append(c)
                    break
                else:
                    k -= num
                    cnt[c] += 1
            else:
                return ""    # fewer than k permutations

        if k > 1:
            return ""

        first_half = "".join(half)
        return first_half + mid + first_half[::-1]
