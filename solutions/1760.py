class Solution:
    def canFormArray(self, arr, pieces):
        # Map first element of each piece to the piece itself
        first_to_piece = {p[0]: p for p in pieces}
        
        i = 0
        n = len(arr)
        while i < n:
            val = arr[i]
            # If there's no piece starting with arr[i], fail
            if val not in first_to_piece:
                return False
            piece = first_to_piece[val]
            length = len(piece)
            # Check if arr[i:i+length] matches the piece
            if arr[i:i+length] != piece:
                return False
            # Advance past this piece
            i += length
        
        # If we've consumed all of arr successfully, it's possible
        return True
