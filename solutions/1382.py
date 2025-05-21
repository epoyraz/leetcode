class Solution:
    def calculateTax(self, brackets, income):
        tax = 0.0
        prev_upper = 0
        
        for upper, pct in brackets:
            if income <= prev_upper:
                break
            # amount taxed in this bracket
            taxable = min(income, upper) - prev_upper
            tax += taxable * pct / 100.0
            prev_upper = upper
        
        return tax
