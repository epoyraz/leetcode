class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        if not word:
            return ""
        
        res = []
        count = 1
        
        # scan from the second character onward
        for i in range(1, len(word)):
            if word[i] == word[i-1] and count < 9:
                # same char and haven't hit the cap yet
                count += 1
            else:
                # either different char or cap reached:
                # flush the run we just counted
                res.append(str(count))
                res.append(word[i-1])
                # start a new run
                count = 1
        
        # flush the final run
        res.append(str(count))
        res.append(word[-1])
        
        return "".join(res)
