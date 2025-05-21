class Solution(object):
    def permute(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        # total odds and evens
        odd_total = (n + 1)//2
        even_total = n//2

        # manual memoization
        dp_memo = {}
        def dp(o, e, last_parity):
            # last_parity: 0=start, 1=odd, 2=even
            if o == 0 and e == 0:
                return 1
            key = (o, e, last_parity)
            if key in dp_memo:
                return dp_memo[key]
            ways = 0
            if last_parity != 1 and o > 0:
                ways += o * dp(o-1, e, 1)
            if last_parity != 2 and e > 0:
                ways += e * dp(o, e-1, 2)
            dp_memo[key] = ways
            return ways

        total = dp(odd_total, even_total, 0)
        if k > total:
            return []

        odds = list(range(1, n+1, 2))
        evens = list(range(2, n+1, 2))
        ans = []
        o_rem, e_rem = odd_total, even_total
        last = 0

        for _ in range(n):
            i = j = 0
            while i < len(odds) or j < len(evens):
                if j == len(evens) or (i < len(odds) and odds[i] < evens[j]):
                    x, parity = odds[i], 1
                    i += 1
                else:
                    x, parity = evens[j], 2
                    j += 1
                if parity == last:
                    continue
                if parity == 1:
                    cnt = dp(o_rem-1, e_rem, 1)
                else:
                    cnt = dp(o_rem, e_rem-1, 2)
                if cnt >= k:
                    ans.append(x)
                    last = parity
                    if parity == 1:
                        odds.pop(i-1)
                        o_rem -= 1
                    else:
                        evens.pop(j-1)
                        e_rem -= 1
                    break
                k -= cnt
            else:
                return []
        return ans
