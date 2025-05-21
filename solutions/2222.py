import math

class Solution:
    def abbreviateProduct(self, left, right):          # no type hints, no f-strings
        # ---------- count powers of 2 and 5 ----------
        pow2 = pow5 = 0
        stripped = []                                  # numbers with 2- and 5-factors removed
        for x in range(left, right + 1):
            t = x
            while t % 2 == 0:
                pow2 += 1
                t //= 2
            while t % 5 == 0:
                pow5 += 1
                t //= 5
            stripped.append(t)

        C = pow2 if pow2 < pow5 else pow5              # trailing-zero count
        pow2 -= C                                      # remaining unpaired 2âs
        pow5 -= C                                      # remaining unpaired 5âs

        # ---------- suffix (last 5 non-zero digits) ----------
        MOD = 1000000000                               # keep 9 tail digits
        tail = 1
        for v in stripped:
            tail = (tail * v) % MOD
        tail = (tail * pow(2, pow2, MOD)) % MOD
        tail = (tail * pow(5, pow5, MOD)) % MOD
        while tail % 10 == 0:
            tail //= 10
        suf = str(tail % 100000).zfill(5)              # exactly 5 digits

        # ---------- prefix (first 5 digits) ----------
        lead = 1
        LIMIT = 10000000000000000                      # 10^16  (keep 16 leading digits)
        for v in stripped:
            lead *= v
            while lead >= LIMIT:                       # trim to 16 digits
                lead //= 10
        for _ in range(pow2):                          # leftover 2âs
            lead *= 2
            while lead >= LIMIT:
                lead //= 10
        for _ in range(pow5):                          # leftover 5âs
            lead *= 5
            while lead >= LIMIT:
                lead //= 10
        pre = (str(lead) + "00000")[:5]               # first 5 digits (pad if needed)

        # ---------- total digit count after removing zeros ----------
        log_sum = 0.0
        for x in range(left, right + 1):
            log_sum += math.log10(x)
        digits = int(log_sum) + 1 - C

        # ---------- if result is small (<=10 digits) compute exactly ----------
        if digits <= 10:
            prod = 1
            for x in range(left, right + 1):
                prod *= x
            while prod % 10 == 0:
                prod //= 10
            return str(prod) + "e" + str(C)

        # ---------- assemble abbreviated form ----------
        return pre + "..." + suf + "e" + str(C)
