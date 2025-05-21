import collections
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        
        route = []
        
        def visit(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                visit(next_airport)
            route.append(airport)
        
        visit('JFK')
        return route[::-1]
