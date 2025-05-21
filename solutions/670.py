class Solution(object):
    def maximumSwap(self, num):
        num = list(str(num))
        last = {int(x): i for i, x in enumerate(num)}
        
        for i, x in enumerate(num):
            for d in range(9, int(x), -1):
                if last.get(d, -1) > i:
                    num[i], num[last[d]] = num[last[d]], num[i]
                    return int(''.join(num))
        
        return int(''.join(num))
