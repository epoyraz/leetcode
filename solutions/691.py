from collections import Counter

class Solution(object):
    def minStickers(self, stickers, target):
        m = len(stickers)
        sticker_count = [Counter(sticker) for sticker in stickers]
        memo = {}
        
        def dfs(remain):
            if remain == "":
                return 0
            if remain in memo:
                return memo[remain]
            
            remain_count = Counter(remain)
            res = float('inf')
            for sc in sticker_count:
                if remain[0] not in sc:
                    continue
                new_remain = ""
                for c in remain_count:
                    if remain_count[c] > sc[c]:
                        new_remain += (c * (remain_count[c] - sc[c]))
                tmp = dfs(new_remain)
                if tmp != -1:
                    res = min(res, 1 + tmp)
            
            memo[remain] = -1 if res == float('inf') else res
            return memo[remain]
        
        return dfs(target)
