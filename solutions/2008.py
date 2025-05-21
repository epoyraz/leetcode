class Solution:
    def minOperationsToFlip(self, expression):
        # ------------------------------------------------------------
        # For every sub-expression we keep a pair (val, flip)
        #   val   : 0 or 1  â  the value of the sub-expression
        #   flip  : minimum operations needed to flip that value
        #
        # For a literal:
        #   '0' â (0, 1)     (flip it by turning it to '1')
        #   '1' â (1, 1)     (flip it by turning it to '0')
        #
        # While combining two sub-expressions we evaluate the operator
        # that is really present and *also* consider flipping it
        # (cost +1) to find the cheapest way to reach both results 0
        # and 1.  Finally we return the cost that flips the actual
        # result.
        # ------------------------------------------------------------
        vals, ops = [], []

        # helper that returns (val, flip) for a âopâ b
        def combine(a, b, op):
            v1, f1 = a
            v2, f2 = b

            # cost to force a (sub-)expression to 0 / 1
            a0 = 0 if v1 == 0 else f1
            a1 = 0 if v1 == 1 else f1
            b0 = 0 if v2 == 0 else f2
            b1 = 0 if v2 == 1 else f2

            if op == '&':
                res = v1 & v2
                # keep '&'
                keep0 = min(a0 + b0, a0 + b1, a1 + b0)
                keep1 = a1 + b1
                # flip to '|'
                flip0 = 1 + (a0 + b0)
                flip1 = 1 + min(a1 + b1, a1 + b0, a0 + b1)
            else:  # op == '|'
                res = v1 | v2
                # keep '|'
                keep0 = a0 + b0
                keep1 = min(a1 + b1, a1 + b0, a0 + b1)
                # flip to '&'
                flip0 = 1 + min(a0 + b0, a0 + b1, a1 + b0)
                flip1 = 1 + (a1 + b1)

            best0 = min(keep0, flip0)
            best1 = min(keep1, flip1)
            flip = best1 if res == 0 else best0
            return (res, flip)

        def apply():
            b = vals.pop()
            a = vals.pop()
            op = ops.pop()
            vals.append(combine(a, b, op))

        for ch in expression:
            if ch in '01':
                vals.append((int(ch), 1))
            elif ch == '(':
                ops.append(ch)
            elif ch in '&|':
                # '&' and '|' have the same precedence and are
                # evaluated left-to-right.
                while ops and ops[-1] in '&|':
                    apply()
                ops.append(ch)
            else:  # ch == ')'
                while ops and ops[-1] != '(':
                    apply()
                ops.pop()          # discard '('

        while ops:
            apply()

        # vals[0] now holds (value, min cost to flip)
        return vals[0][1]
