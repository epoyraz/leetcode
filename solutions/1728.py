class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        # Sequence of tuples: (val, mul_at_append, add_at_append, inv_mul_at_append)
        self.data = []
        # Global affine transformation parameters:
        #   x -> x * curr_mul + curr_add
        self.curr_mul = 1
        self.curr_add = 0
        # Maintain inverse of curr_mul so we can "undo" prefix multipliers
        self.inv_mul = 1

    def append(self, val):
        # Record the raw val and the current transformation state
        self.data.append((
            val,
            self.curr_mul,
            self.curr_add,
            self.inv_mul
        ))

    def addAll(self, inc):
        # x -> x + inc
        self.curr_add = (self.curr_add + inc) % self.MOD

    def multAll(self, m):
        # x -> x * m
        self.curr_mul = self.curr_mul * m % self.MOD
        self.curr_add = self.curr_add * m % self.MOD
        # Update inv_mul *= inverse(m) mod
        inv_m = pow(m, self.MOD - 2, self.MOD)
        self.inv_mul = self.inv_mul * inv_m % self.MOD

    def getIndex(self, idx):
        if idx < 0 or idx >= len(self.data):
            return -1

        val, mul0, add0, inv_mul0 = self.data[idx]
        # Compute the net multiplier since append:
        #   gm_ratio = curr_mul / mul0  mod => curr_mul * inv(mul0)
        gm_ratio = self.curr_mul * inv_mul0 % self.MOD
        # Compute the net addition:
        #   ga_ratio = curr_add - add0 * gm_ratio
        ga_ratio = (self.curr_add - add0 * gm_ratio) % self.MOD

        # Apply to the raw value
        return (val * gm_ratio + ga_ratio) % self.MOD
