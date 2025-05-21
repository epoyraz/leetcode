import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        # Map food -> current rating
        self.food_rating = {}
        # Map food -> its cuisine
        self.food_cuisine = {}
        # Map cuisine -> max-heap of (-rating, food)
        self.cuisine_heaps = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_rating[food] = rating
            self.food_cuisine[food] = cuisine
            if cuisine not in self.cuisine_heaps:
                self.cuisine_heaps[cuisine] = []
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        # Update the rating and push new entry onto the cuisine heap
        cuisine = self.food_cuisine[food]
        self.food_rating[food] = newRating
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_heaps[cuisine]
        # Clean up outdated entries
        while heap:
            neg_rating, food = heap[0]
            # If the rating matches current, it's valid
            if -neg_rating == self.food_rating[food]:
                return food
            # Otherwise discard
            heapq.heappop(heap)
        return ""  # Should never happen per problem constraints
