class Solution:
    def destCity(self, paths):
        departure_cities = set(cityA for cityA, _ in paths)
        for _, cityB in paths:
            if cityB not in departure_cities:
                return cityB
