class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        # Start with initial word
        word = 'a'
        # Keep performing the operation until word length covers k
        while len(word) < k:
            # Generate shifted string: each character moves to next in the alphabet, with 'z' -> 'a'
            shifted = ''.join(
                chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
                for c in word
            )
            # Append the shifted string to the original
            word += shifted
        # Return the k-th character (1-based index)
        return word[k-1]