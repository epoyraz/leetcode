class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        i, j = len(arr1) - 1, len(arr2) - 1
        res = []
        carry = 0

        while i >= 0 or j >= 0 or carry != 0:
            a = arr1[i] if i >= 0 else 0
            b = arr2[j] if j >= 0 else 0
            total = a + b + carry
            res.append(total & 1)  # total % 2
            # Update carry based on base -2
            carry = -(total >> 1)
            i -= 1
            j -= 1

        # Remove leading zeros
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return res[::-1]
