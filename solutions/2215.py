class Solution:
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        result = set()
        
        # Precompute indices by digit properties
        nonzero_indices = [i for i, d in enumerate(digits) if d != 0]
        even_indices = [i for i, d in enumerate(digits) if d % 2 == 0]
        
        for i in nonzero_indices:
            for j in range(n):
                if j == i:
                    continue
                for k in even_indices:
                    if k == i or k == j:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    result.add(num)
        
        return sorted(result)
