from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        graph = defaultdict(list)
        indegree = {}
        can_make = set(supplies)

        for rcp, ing in zip(recipes, ingredients):
            indegree[rcp] = len(ing)
            for ing_item in ing:
                graph[ing_item].append(rcp)

        queue = deque(supplies)
        result = []

        while queue:
            item = queue.popleft()
            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
                    result.append(recipe)

        return result
