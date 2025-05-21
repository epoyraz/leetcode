import collections

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [collections.Counter()]
        i, n = 0, len(formula)
        
        while i < n:
            ch = formula[i]
            if ch == '(':
                # Start a new group
                stack.append(collections.Counter())
                i += 1
            elif ch == ')':
                # End current group; pop and apply multiplier
                top = stack.pop()
                i += 1
                # Parse multiplier (if any)
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mul = int(formula[start:i] or 1)
                # Merge into previous level
                for atom, cnt in top.items():
                    stack[-1][atom] += cnt * mul
            else:
                # Parse atom name
                # Uppercase letter
                start = i
                i += 1
                # Following lowercase letters
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                # Parse count (if any)
                start_count = i
                while i < n and formula[i].isdigit():
                    i += 1
                cnt = int(formula[start_count:i] or 1)
                # Add to current level
                stack[-1][atom] += cnt
        
        # Final counts in stack[0]
        counts = stack.pop()
        # Build output: sorted atom names
        atoms = sorted(counts.keys())
        res = []
        for atom in atoms:
            res.append(atom)
            if counts[atom] > 1:
                res.append(str(counts[atom]))
        return "".join(res)
