import collections

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        stop_to_buses = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)
        
        queue = collections.deque()
        visited_buses = set()
        visited_stops = set()
        queue.append((source, 0))
        
        while queue:
            stop, buses = queue.popleft()
            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))
        return -1
