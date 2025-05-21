class Solution:
    def isSolvable(self, words, result):
        weight = {}
        leading = set()

        # Build weights for each character
        for w in words:
            if len(w) > 1:
                leading.add(w[0])
            mul = 1
            for c in reversed(w):
                weight[c] = weight.get(c, 0) + mul
                mul *= 10

        if len(result) > 1:
            leading.add(result[0])
        mul = 1
        for c in reversed(result):
            weight[c] = weight.get(c, 0) - mul
            mul *= 10

        chars = list(weight.keys())
        # Sort by descending absolute weight
        chars.sort(key=lambda c: -abs(weight[c]))
        n = len(chars)

        # Precompute remaining possible sum bounds for pruning
        pos_weights = [weight[c] for c in chars]
        rem_max = [0] * (n + 1)
        rem_min = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            w9 = pos_weights[i] * 9
            rem_max[i] = rem_max[i + 1] + max(0, w9)
            rem_min[i] = rem_min[i + 1] + min(0, w9)

        used = [False] * 10

        def dfs(idx, curr_sum):
            # Prune if even best/worst assignments can't reach zero
            if curr_sum + rem_min[idx] > 0 or curr_sum + rem_max[idx] < 0:
                return False
            if idx == n:
                return curr_sum == 0

            w = pos_weights[idx]
            c = chars[idx]
            for d in range(10):
                if used[d] or (d == 0 and c in leading):
                    continue
                used[d] = True
                if dfs(idx + 1, curr_sum + w * d):
                    return True
                used[d] = False
            return False

        return dfs(0, 0)
