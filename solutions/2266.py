class Solution:
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        def cost_to_type(s, digits):
            pos = str(s)
            total = 0
            for d in pos:
                d = int(d)
                if d != digits[0]:
                    total += moveCost
                    digits[0] = d
                total += pushCost
            return total
        
        res = float('inf')
        for m in range(100):
            s = targetSeconds - m * 60
            if 0 <= s <= 99:
                digits = []
                digits.extend(divmod(m, 10))
                digits.extend(divmod(s, 10))
                while digits and digits[0] == 0:
                    digits.pop(0)
                if not digits:
                    digits = [0]
                cost = 0
                pos = startAt
                for d in digits:
                    if d != pos:
                        cost += moveCost
                    cost += pushCost
                    pos = d
                res = min(res, cost)
        return res
