class Solution:
    def discountPrices(self, sentence, discount):
        parts = sentence.split(" ")
        factor = (100 - discount) / 100.0
        
        for i, w in enumerate(parts):
            if len(w) >= 2 and w[0] == '$' and w[1:].isdigit():
                price = int(w[1:])
                new_price = price * factor
                # Use format() instead of f-string
                parts[i] = "$" + "{:.2f}".format(new_price)
        
        return " ".join(parts)
