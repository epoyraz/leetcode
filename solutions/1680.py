class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        MOD = 10**9 + 7
        n = len(locations)
        memo = {}
        
        def dfs(city, rem):
            if (city, rem) in memo:
                return memo[(city, rem)]
            ways = 1 if city == finish else 0
            for nxt in range(n):
                if nxt != city:
                    cost = abs(locations[city] - locations[nxt])
                    if cost <= rem:
                        ways = (ways + dfs(nxt, rem - cost)) % MOD
            memo[(city, rem)] = ways
            return ways
        
        return dfs(start, fuel)
