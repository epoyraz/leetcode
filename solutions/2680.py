class Solution:
    def monkeyMove(self, n):
        MOD = 10**9 + 7
        return (pow(2, n, MOD) - 2) % MOD
