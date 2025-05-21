class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        filtered = []
        for r in restaurants:
            id_, rating, vegan, price, dist = r
            if veganFriendly and not vegan:
                continue
            if price > maxPrice or dist > maxDistance:
                continue
            filtered.append((rating, id_))
        # Sort by rating desc, id desc
        filtered.sort(key=lambda x: (-x[0], -x[1]))
        return [id_ for _, id_ in filtered]
