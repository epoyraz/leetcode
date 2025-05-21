class Solution(object):
    def splitIntoFibonacci(self, num):
        res = []

        def backtrack(index):
            if index == len(num) and len(res) >= 3:
                return True
            for i in range(index, len(num)):
                if num[index] == '0' and i > index:
                    break
                n = int(num[index:i+1])
                if n >= 2**31:
                    break
                if len(res) >= 2 and res[-1] + res[-2] != n:
                    if res[-1] + res[-2] < n:
                        break
                    continue
                res.append(n)
                if backtrack(i+1):
                    return True
                res.pop()
            return False

        backtrack(0)
        return res
