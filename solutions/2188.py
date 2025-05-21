class Solution:
    def minimizedMaximum(self, n, quantities):
        """
        :param n: int       # number of stores
        :param quantities: List[int]  # quantities[i] = count of product type i
        :return: int        # minimum possible maximum products per store
        """
        def needed_stores(cap):
            # For a given maximum load cap, compute how many stores are needed:
            # each product type i must be split into ceil(quantities[i]/cap) stores.
            total = 0
            for q in quantities:
                # Ceil division without floating:
                total += (q + cap - 1) // cap
                if total > n:  # early exit if already exceeds available stores
                    return total
            return total

        # Binary search on answer x = maximum load per store
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if needed_stores(mid) <= n:
                # mid is feasible: try smaller
                right = mid
            else:
                # mid too small (requires too many stores): increase
                left = mid + 1
        return left