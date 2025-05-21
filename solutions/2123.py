class Solution:
    def numberOfWeakCharacters(self, properties):
        # Sort by descending attack, and ascending defense
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        max_def = 0
        weak = 0

        for attack, defense in properties:
            if defense < max_def:
                weak += 1
            else:
                max_def = defense
        
        return weak
