class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            seen.add(''.join(morse[ord(c) - ord('a')] for c in word))
        return len(seen)
