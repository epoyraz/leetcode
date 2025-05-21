class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        MOD = 10**9 + 7

        def dec_str(s):
            # subtract 1 from decimal string s (s represents integer >= 1)
            lst = list(s)
            i = len(lst) - 1
            while i >= 0:
                if lst[i] == '0':
                    lst[i] = '9'
                    i -= 1
                else:
                    lst[i] = str(ord(lst[i]) - ord('0') - 1)
                    break
            res = ''.join(lst).lstrip('0')
            return res if res else "0"

        def count_upto(s):
            digits = list(map(int, s))
            n = len(digits)
            memo = {}

            def dfs(pos, last, tight, started):
                # pos: current index in digits
                # last: last digit used (or -1 if not started)
                # tight: whether we are matching prefix of s
                # started: whether we've placed a nonzero and begun the number
                if pos == n:
                    return 1 if started else 0

                key = (pos, last, tight, started)
                if key in memo:
                    return memo[key]

                limit = digits[pos] if tight else 9
                ans = 0

                for d in range(0, limit + 1):
                    ntight = tight and (d == limit)
                    if not started:
                        # still skipping leading zeros
                        if d == 0:
                            ans += dfs(pos + 1, -1, ntight, False)
                        else:
                            # start the number here
                            ans += dfs(pos + 1, d, ntight, True)
                    else:
                        # already started: enforce |d-last| == 1
                        if abs(d - last) == 1:
                            ans += dfs(pos + 1, d, ntight, True)
                        # else skip

                ans %= MOD
                memo[key] = ans
                return ans

            return dfs(0, -1, True, False)

        low_minus = dec_str(low)
        res = count_upto(high) - count_upto(low_minus)
        return res % MOD
