class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            suggestions = []
            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)
                if len(suggestions) == 3:
                    break
            res.append(suggestions)
        return res
