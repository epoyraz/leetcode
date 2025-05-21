class Solution:
    def categorizeBox(self, length, width, height, mass):
        # Determine if the box is bulky
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or length * width * height >= 10**9:
            bulky = True
        else:
            bulky = False
        
        # Determine if the box is heavy
        heavy = mass >= 100
        
        # Return category based on both flags
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"
