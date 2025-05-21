class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        # Build evaluation map
        evalmap = dict(zip(evalvars, evalints))

        # Tokenize the expression
        tokens = []
        i, n = 0, len(expression)
        while i < n:
            c = expression[i]
            if c == ' ':
                i += 1
            elif c in '+-*()':
                tokens.append(c)
                i += 1
            else:
                j = i
                while j < n and expression[j].isalnum():
                    j += 1
                tokens.append(expression[i:j])
                i = j

        # Polynomial arithmetic on dicts mapping varâtuples â coefficient
        def add_poly(A, B):
            C = A.copy()
            for k, v in B.items():
                C[k] = C.get(k, 0) + v
                if C[k] == 0:
                    del C[k]
            return C

        def sub_poly(A, B):
            C = A.copy()
            for k, v in B.items():
                C[k] = C.get(k, 0) - v
                if C[k] == 0:
                    del C[k]
            return C

        def mul_poly(A, B):
            C = {}
            for ka, va in A.items():
                for kb, vb in B.items():
                    key = tuple(sorted(ka + kb))
                    C[key] = C.get(key, 0) + va * vb
                    if C[key] == 0:
                        del C[key]
            return C

        # Recursiveâdescent parser
        def parse_expr(idx):
            # expr := term { (+ | -) term }
            res, idx = parse_term(idx)
            while idx < len(tokens) and tokens[idx] in ('+', '-'):
                op = tokens[idx]
                rhs, idx = parse_term(idx + 1)
                if op == '+':
                    res = add_poly(res, rhs)
                else:
                    res = sub_poly(res, rhs)
            return res, idx

        def parse_term(idx):
            # term := factor { * factor }
            res, idx = parse_factor(idx)
            while idx < len(tokens) and tokens[idx] == '*':
                rhs, idx = parse_factor(idx + 1)
                res = mul_poly(res, rhs)
            return res, idx

        def parse_factor(idx):
            tok = tokens[idx]
            if tok == '(':
                # parenthesized subâexpression
                sub, idx2 = parse_expr(idx + 1)
                return sub, idx2 + 1  # skip ')'
            else:
                # number or variable
                if tok.isdigit():
                    poly = {(): int(tok)}
                elif tok in evalmap:
                    poly = {(): evalmap[tok]}
                else:
                    poly = {(tok,): 1}
                return poly, idx + 1

        # Parse and evaluate
        poly, _ = parse_expr(0)

        # Format output: sort by degree desc, then lex order
        items = sorted(poly.items(),
                       key=lambda kv: (-len(kv[0]), kv[0]))
        result = []
        for vars_tuple, coeff in items:
            if coeff == 0:
                continue
            s = str(coeff)
            if vars_tuple:
                s += '*' + '*'.join(vars_tuple)
            result.append(s)
        return result
