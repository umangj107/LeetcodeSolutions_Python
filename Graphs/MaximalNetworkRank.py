from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        road_dict = defaultdict(list)
        for road in roads:
            road_dict[road[0]].append(road[1])
            road_dict[road[1]].append(road[0])
        first = 0
        second = 0
        first_roads = []
        second_roads = []
        for road, peers in road_dict.items():
            if first <= len(peers):
                if not first_roads or first < len(peers):
                    second = first
                    second_roads = first_roads
                    first = len(peers)
                    first_roads = [road]
                else:
                    first_roads.append(road)
            elif second <= len(peers):
                if not second_roads or second < len(peers):
                    second = len(peers)
                    second_roads = [road]
                else:
                    second_roads.append(road)
        if len(first_roads) > 1:
            for i in range(len(first_roads)-1):
                cur = i
                for j in range(i+1, len(first_roads)):
                    if first_roads[cur] not in road_dict[first_roads[j]]:
                        return first*2
            return first*2-1
        else:
            for f in first_roads:
                for s in second_roads:
                    if s not in road_dict[f]:
                        return first+second
            return first+second-1
