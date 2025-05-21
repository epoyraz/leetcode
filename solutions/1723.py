class Solution:
    def maximumRequests(self, n, requests):
        m = len(requests)
        # Precompute all subset masks
        masks = list(range(1 << m))
        # Sort subsets by size (number of requests chosen) descending
        masks.sort(key=lambda mask: bin(mask).count('1'), reverse=True)

        for mask in masks:
            k = bin(mask).count('1')
            # If even the largest remaining subset can't beat 0, we can stop early
            if k == 0:
                break

            # Track net transfer balance for each building
            bal = [0] * n
            for i in range(m):
                if (mask >> i) & 1:
                    frm, to = requests[i]
                    bal[frm] -= 1
                    bal[to]  += 1

            # If all balances zero, this subset is valid
            if all(x == 0 for x in bal):
                return k

        return 0
