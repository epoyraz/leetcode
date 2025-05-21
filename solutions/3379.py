class Solution:
    def scoreOfString(self, s: str) -> int:
        # Initialize the score
        score = 0
        
        # Iterate through the string, calculating the absolute difference between adjacent characters
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        
        return score        