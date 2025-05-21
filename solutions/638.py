class Solution(object):
    def shoppingOffers(self, price, special, needs):
        memo = {}
        
        def dfs(cur_needs):
            if tuple(cur_needs) in memo:
                return memo[tuple(cur_needs)]
            
            res = sum(cur_needs[i] * price[i] for i in range(len(price)))
            
            for offer in special:
                new_needs = []
                for i in range(len(price)):
                    if cur_needs[i] < offer[i]:
                        break
                    new_needs.append(cur_needs[i] - offer[i])
                else:
                    res = min(res, offer[-1] + dfs(new_needs))
                    
            memo[tuple(cur_needs)] = res
            return res
        
        return dfs(needs)
