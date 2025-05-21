class Spreadsheet(object):
    def __init__(self, rows):
        """
        :type rows: int
        """
        # We don't actually need to track rows beyond validation,
        # since constraints guarantee valid references.
        # Store only explicitly set cells in a dict.
        self.cells = {}

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        # Store the integer value for this cell reference.
        # Cell is like "A1", "Z1000"
        self.cells[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        # Reset to 0 by removing from dict if present.
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        # formula is always "=X+Y"
        expr = formula[1:]         # remove leading '='
        left, right = expr.split('+')
        
        def val(token):
            # If token starts with a letter, it's a cell reference
            if token[0].isalpha():
                return self.cells.get(token, 0)
            else:
                # Otherwise it's a non-negative integer
                return int(token)
        
        return val(left) + val(right)
