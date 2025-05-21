class Solution:
    def countAnagrams(self, s):
        mod = 10**9 + 7
        
        # Split into words
        words = s.split(' ')
        # Find maximum word length to size our factorial table
        max_len = max(len(w) for w in words)
        
        # Precompute factorials mod and inverse factorials mod
        fact = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            fact[i] = fact[i - 1] * i % mod
        
        invf = [1] * (max_len + 1)
        invf[max_len] = pow(fact[max_len], mod - 2, mod)
        for i in range(max_len, 0, -1):
            invf[i - 1] = invf[i] * i % mod
        
        ans = 1
        # For each word, multiply by permutations = L! / (â freq[c]!)
        for w in words:
            L = len(w)
            ans = ans * fact[L] % mod
            
            # Count character frequencies
            freq = {}
            for ch in w:
                freq[ch] = freq.get(ch, 0) + 1
            
            # Divide out duplicate permutations
            for f in freq.values():
                ans = ans * invf[f] % mod
        
        return ans
