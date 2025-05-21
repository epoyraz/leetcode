class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}
        
        def ways(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    left = ways(expr[:i])
                    right = ways(expr[i+1:])
                    for l in left:
                        for r in right:
                            if expr[i] == '+':
                                res.append(l + r)
                            elif expr[i] == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)
            if not res:
                res.append(int(expr))
            memo[expr] = res
            return res
        
        return ways(expression)
