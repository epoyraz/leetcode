from collections import Counter

class Solution(object):
    def sortString(self, s):
        count = Counter(s)
        result = []
        
        while len(result) < len(s):
            # Step 1â3: ascending order
            for c in sorted(count.keys()):
                if count[c] > 0:
                    result.append(c)
                    count[c] -= 1
            # Step 4â6: descending order
            for c in sorted(count.keys(), reverse=True):
                if count[c] > 0:
                    result.append(c)
                    count[c] -= 1

        return ''.join(result)
