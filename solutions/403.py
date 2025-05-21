class Solution:
    def canCross(self, stones):
        stone_set = set(stones)
        last_stone = stones[-1]
        dp = {0: {0}}
        
        for stone in stones:
            for jump in dp.get(stone, set()):
                for next_jump in (jump - 1, jump, jump + 1):
                    if next_jump > 0 and stone + next_jump in stone_set:
                        if stone + next_jump not in dp:
                            dp[stone + next_jump] = set()
                        dp[stone + next_jump].add(next_jump)
        
        return last_stone in dp
