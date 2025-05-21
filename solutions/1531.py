class Solution:
    def numberWays(self, hats):
        from collections import defaultdict
        MOD = 10**9 + 7
        n = len(hats)

        # Build mapping from hat to list of people who like it
        hat_to_people = defaultdict(list)
        for person, hat_list in enumerate(hats):
            for hat in hat_list:
                hat_to_people[hat].append(person)

        # dp[mask] = number of ways to assign hats with current mask of assigned people
        dp = [0] * (1 << n)
        dp[0] = 1

        for hat in range(1, 41):
            if hat not in hat_to_people:
                continue

            ndp = dp[:]
            for mask in range(1 << n):
                if dp[mask] == 0:
                    continue
                for person in hat_to_people[hat]:
                    if not (mask & (1 << person)):
                        ndp[mask | (1 << person)] = (ndp[mask | (1 << person)] + dp[mask]) % MOD
            dp = ndp

        return dp[(1 << n) - 1]
