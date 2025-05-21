class Solution(object):
    def distMoney(self, money, children):
        # 1) Must give at least $1 to each child
        if money < children:
            return -1
        
        # 2) Strip off the $1 per child
        rem = money - children
        
        # 3) Greedily give as many â+7â (to make $8 total) as possible
        res = min(children, rem // 7)
        
        # 4) If we gave all children their 8 but still have leftover,
        #    that leftover can't be assigned, so drop one 8
        if res == children and rem != 7 * children:
            res -= 1
        
        # 5) Finally, avoid the âone child gets exactly $4â trap:
        #    if after giving resÃ7 extra, the single remaining kid
        #    would end up with 1+3=4, we must reduce res by 1
        if children - res == 1 and rem - res * 7 == 3:
            res -= 1
        
        return res
