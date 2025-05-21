class Solution:
    def minOperations(self, logs):
        depth = 0
        for op in logs:
            if op == "../":
                if depth > 0:
                    depth -= 1
            elif op == "./":
                continue
            else:
                # any "x/" entry
                depth += 1
        return depth
