class Solution:
    def oddString(self, words):
        def diff_sig(w):
            # Compute the tuple of differences for word w
            return tuple(ord(w[i+1]) - ord(w[i]) for i in range(len(w)-1))
        
        # Compute signatures for the first three words
        sig0 = diff_sig(words[0])
        sig1 = diff_sig(words[1])
        sig2 = diff_sig(words[2])
        
        # Determine the common signature by majority among the first three
        if sig0 == sig1 or sig0 == sig2:
            common = sig0
        else:
            common = sig1
        
        # Find and return the word whose signature differs
        for w in words:
            if diff_sig(w) != common:
                return w
        # Problem guarantees one exists, so we never reach here
