class ATM:
    def __init__(self):
        # counts for [20, 50, 100, 200, 500]
        self.counts = [0] * 5
        self.denoms = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        # Add the deposited banknotes to the machine
        for i in range(5):
            self.counts[i] += banknotesCount[i]

    def withdraw(self, amount):
        # Try to greedily use largest denominations first
        to_use = [0] * 5
        remaining = amount

        for i in range(4, -1, -1):
            # maximum we could use of denom i
            max_notes = remaining // self.denoms[i]
            use = min(self.counts[i], max_notes)
            to_use[i] = use
            remaining -= use * self.denoms[i]

        # If we couldn't make the exact amount, reject
        if remaining != 0:
            return [-1]

        # Otherwise commit the withdrawal
        for i in range(5):
            self.counts[i] -= to_use[i]

        return to_use
