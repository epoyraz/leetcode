class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        # If there's only one friend, they get the whole word
        if numFriends == 1:
            return word
        
        n = len(word)
        # Maximum length any one piece can have
        max_len = n - numFriends + 1
        
        # Find the global largest character
        max_char = max(word)
        
        best = ""
        for i, ch in enumerate(word):
            if ch == max_char:
                # take the longest substring starting here
                candidate = word[i:i + max_len]
                if candidate > best:
                    best = candidate
        return best
