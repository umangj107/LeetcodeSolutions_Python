class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        all_pairs = {}
        for p in pairs:
            all_pairs[p[0]] = p[1]
            all_pairs[p[1]] = p[0]
        rank_maps = []
        for p in preferences:
            rank_map = {}
            for i in range(n-1):
                rank_map[p[i]] = i
            rank_maps.append(rank_map)
        res = 0
        for (x, y) in all_pairs.items():
            # This condition means its a happy friend and no need of further checks
            if preferences[x][0] == y:
                continue
            for i in range(n-1):
                u = preferences[x][i]
                if u != y:
                    if rank_maps[x][u] < rank_maps[x][y] and rank_maps[u][x] < rank_maps[u][all_pairs[u]]:
                        res += 1
                        break
        return res
