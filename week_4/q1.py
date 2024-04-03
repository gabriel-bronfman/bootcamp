class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        stop_to_buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1
        if source == target:
            return 0   
        queue = deque([source])
        buses_taken = set()
        stops_visited = set()
        res = 0
        while queue:  
            res += 1
            stops_to_process = len(queue)
            for _ in range(stops_to_process):
                current_stop = queue.popleft()
                for bus_id in stop_to_buses[current_stop]:
                    if bus_id in buses_taken:
                        continue
                    buses_taken.add(bus_id)
                    for next_stop in routes[bus_id]:
                        if next_stop in stops_visited:
                            continue
                        if next_stop == target:
                            return res
                        stops_visited.add(next_stop)


        return -1