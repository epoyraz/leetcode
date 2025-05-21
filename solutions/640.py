class Solution(object):
    def solveEquation(self, equation):
        def parse(side):
            coef = 0
            const = 0
            i = 0
            sign = 1
            while i < len(side):
                if side[i] == '+':
                    sign = 1
                    i += 1
                elif side[i] == '-':
                    sign = -1
                    i += 1
                else:
                    num = 0
                    is_num = False
                    while i < len(side) and side[i].isdigit():
                        num = num * 10 + int(side[i])
                        i += 1
                        is_num = True
                    if i < len(side) and side[i] == 'x':
                        if not is_num:
                            num = 1
                        coef += sign * num
                        i += 1
                    else:
                        const += sign * num
            return coef, const
        
        left, right = equation.split('=')
        lcoef, lconst = parse(left)
        rcoef, rconst = parse(right)
        
        coef = lcoef - rcoef
        const = rconst - lconst
        
        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(const // coef)
