class Solution:
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if rows == 1 or not encodedText:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # 1) Build the matrix row-wise
        M = [list(encodedText[i*cols:(i+1)*cols]) for i in range(rows)]
        
        # 2) Read out along the slanted diagonals
        res = []
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                res.append(M[r][c])
                r += 1
                c += 1
        
        # 3) Strip any trailing spaces and return
        return "".join(res).rstrip()
