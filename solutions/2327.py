class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Convert to list of digits (as strings)
        digits = list(str(num))
        
        # Extract and sort evens and odds in descending order
        evens = sorted((d for d in digits if int(d) % 2 == 0), reverse=True)
        odds  = sorted((d for d in digits if int(d) % 2 == 1), reverse=True)
        
        # Pointers into the sorted lists
        e = o = 0
        res = []
        
        # Rebuild the number by picking the largest available digit of the same parity
        for d in digits:
            if int(d) % 2 == 0:
                res.append(evens[e])
                e += 1
            else:
                res.append(odds[o])
                o += 1
        
        # Join and convert back to int
        return int("".join(res))
