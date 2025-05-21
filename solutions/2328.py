class Solution:
    def minimizeResult(self, expression):
        left, right = expression.split('+')
        best_val = float('inf')
        best_expr = None

        # Try every place to put '(' in left, and ')' in right
        for i in range(len(left)):           # i = 0 means "(" before left[0]
            for j in range(1, len(right) + 1):  # j = len(right) means ")" after right[-1]
                prefix       = left[:i]
                inside_left  = left[i:]
                inside_right = right[:j]
                suffix       = right[j:]

                # Multipliers: absent prefix/suffix means multiply by 1
                P = int(prefix) if prefix else 1
                S = int(suffix) if suffix else 1

                total = P * (int(inside_left) + int(inside_right)) * S

                if total < best_val:
                    best_val  = total
                    best_expr = prefix + "(" + inside_left + "+" + inside_right + ")" + suffix

        return best_expr
