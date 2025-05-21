class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(index, path, value, prev):
            if index == len(num):
                if value == target:
                    res.append(path)
                return
            
            for i in range(index+1, len(num)+1):
                temp = num[index:i]
                if len(temp) > 1 and temp[0] == '0':
                    break
                curr = int(temp)
                if index == 0:
                    backtrack(i, temp, curr, curr)
                else:
                    backtrack(i, path + '+' + temp, value + curr, curr)
                    backtrack(i, path + '-' + temp, value - curr, -curr)
                    backtrack(i, path + '*' + temp, value - prev + prev * curr, prev * curr)
        
        backtrack(0, '', 0, 0)
        return res
