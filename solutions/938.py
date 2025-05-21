class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        n_str = str(n)
        n_len = len(n_str)
        d_len = len(digits)
        
        total = 0
        for i in range(1, n_len):
            total += d_len ** i
        
        for i in range(n_len):
            smaller = sum(c < n_str[i] for c in digits)
            total += smaller * (d_len ** (n_len - i - 1))
            if n_str[i] not in digits:
                return total
        return total + 1
