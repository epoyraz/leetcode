class Solution:
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        
        if len(seats) < 2 or len(seats) % 2 != 0:
            return 0

        ways = 1
        for i in range(2, len(seats), 2):
            gap = seats[i] - seats[i - 1]
            ways = (ways * gap) % MOD

        return ways
