class Solution:
    def largestVariance(self, s):
        # Convert string to list of ints 0..25 for speed
        n = len(s)
        s_int = [ord(c) - ord('a') for c in s]
        
        # Determine which characters actually appear
        present = [False]*26
        for c in s_int:
            present[c] = True
        letters = [i for i, ok in enumerate(present) if ok]
        
        best = 0
        
        # For each ordered pair (major, minor)
        for x in letters:
            for y in letters:
                if x == y:
                    continue
                
                # Forward scan
                diff = 0
                have_y = False
                for c in s_int:
                    if c == x:
                        diff += 1
                    elif c == y:
                        diff -= 1
                        have_y = True
                    if have_y and diff > best:
                        best = diff
                    if diff < 0:
                        diff = 0
                        have_y = False
                
                # Backward scan
                diff = 0
                have_y = False
                for c in reversed(s_int):
                    if c == x:
                        diff += 1
                    elif c == y:
                        diff -= 1
                        have_y = True
                    if have_y and diff > best:
                        best = diff
                    if diff < 0:
                        diff = 0
                        have_y = False
        
        return best
