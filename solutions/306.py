class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        
        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                n1, n2 = int(num1), int(num2)
                k = j
                while k < n:
                    n3 = n1 + n2
                    n3_str = str(n3)
                    if not num.startswith(n3_str, k):
                        break
                    k += len(n3_str)
                    n1, n2 = n2, n3
                if k == n:
                    return True
        return False
